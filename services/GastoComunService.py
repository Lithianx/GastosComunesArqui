from models.GastoComunModel import GastoComun,db


class GastoComunService:
    @staticmethod
    def generar_pago(num_depto, monto, periodo, fecha_pago, estado_pago="pendiente"):
        # Verificar si ya existe un gasto común para el mismo num_depto y periodo
        gasto_existente = GastoComun.query.filter_by(num_depto=num_depto, periodo=periodo).first()
        if gasto_existente:
            raise ValueError("Ya existe un gasto común para este departamento en el mismo periodo.")


    @staticmethod
    def marcar_pago(id_gasto_comun, estado_pago):
        pago = GastoComun.query.get(id_gasto_comun)
        if pago:
            pago.estado_pago = estado_pago
            db.session.commit()
        return pago

    @staticmethod
    def obtener_pago(id_gasto_comun):
        return GastoComun.query.get(id_gasto_comun)