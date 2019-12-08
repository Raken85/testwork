from testwork import db
from sqlalchemy import func


class Cpu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usage = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Cpu {}>'.format(self.usage)

    @staticmethod
    def sort(field, direction):
        return Cpu.query.order_by(getattr(db, direction)(getattr(Cpu, field)))

    @staticmethod
    def min(limit=None):
        if limit is not None:
            cnt = db.session.query(func.count(Cpu.id)).scalar()
            return db.session.query(func.min(Cpu.usage)).filter(Cpu.id.between(cnt - limit, cnt)).first()
        return db.session.query(func.min(Cpu.usage)).first()

    @staticmethod
    def max(limit=None):
        if limit is not None:
            cnt = db.session.query(func.count(Cpu.id)).scalar()
            return db.session.query(func.max(Cpu.usage)).filter(Cpu.id.between(cnt - limit, cnt)).first()
        return db.session.query(func.max(Cpu.usage)).first()

    @staticmethod
    def avg(limit=None):
        if limit is not None:
            cnt = db.session.query(func.count(Cpu.id)).scalar()
            return db.session.query(func.avg(Cpu.usage)).filter(Cpu.id.between(cnt - limit, cnt)).first()
        return db.session.query(func.avg(Cpu.usage)).first()

    def to_dict(self):
        data = {
            'id': self.id,
            'usage': self.usage
        }
        return data

    def from_dict(self, data):
        for field in ['usage']:
            if field in data:
                setattr(self, field, data[field])
