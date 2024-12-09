from app import db

class GastoComun(db.Model):
    __tablename__ = 'gastos_comunes'

    id = db.Column(db.Integer, primary_key=True)
    num_depto = db.Column(db.Integer, nullable=False)
    monto = db.Column(db.Float, nullable=False)
    periodo = db.Column(db.String(20), nullable=False)
    fecha_pago = db.Column(db.String(20), nullable=True)
    estado_pago = db.Column(db.String(10), nullable=False) 


    def serialize(self):
        """Convierte la instancia en un diccionario para facilitar la conversión a JSON."""
        return {
            "id": self.id,
            "num_depto": self.num_depto,
            "monto": self.monto,
            "periodo": self.periodo,
            "fecha_pago": self.fecha_pago,
            "estado_pago": self.estado_pago
        }