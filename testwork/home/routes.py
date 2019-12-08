from flask import render_template, request, url_for, current_app, session
from testwork.models import Cpu
from testwork.home import bp


@bp.route('/index')
@bp.route('/index.html')
@bp.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    if 'sort' in session:
        sort = session.get('sort')
    else:
        sort = {'field': 'id', 'direction': 'desc'}
    if request.method == 'POST':
        sort = session['sort'] = {'field': request.form['field'], 'direction': request.form['direction']}
        cpus = Cpu.sort(sort['field'], sort['direction']).paginate(page, current_app.config['CPU_USAGE_PER_PAGE'], False)
        return render_template('cpu.html', cpus=cpus.items, sort=sort)
    cpus = Cpu.sort(sort['field'], sort['direction']).paginate(page, current_app.config['CPU_USAGE_PER_PAGE'], False)
    next_url = url_for('home.index', page=cpus.next_num) if cpus.has_next else None
    prev_url = url_for('home.index', page=cpus.prev_num) if cpus.has_prev else None
    min = {'all': Cpu.min()[0], 'limit': Cpu.min(limit=99)[0]}
    max = {'all': Cpu.max()[0], 'limit': Cpu.max(limit=99)[0]}
    avg = {'all': Cpu.avg()[0], 'limit': Cpu.avg(limit=99)[0]}
    return render_template('index.html', title='CPU Usage', cpus=cpus.items, next_url=next_url, prev_url=prev_url,
                           min=min, max=max, avg=avg, sort=sort)
