from services.GastoComunService import GastoComunService

class GastoComunController:
    @staticmethod
    def generar_pago_controller(num_depto, monto, periodo, fecha_pago, estado_pago):
        try:
            return GastoComunService.generar_pago(num_depto, monto, periodo, fecha_pago, estado_pago)
        except ValueError as e:
            
            raise ValueError(str(e))

    @staticmethod
    def marcar_pago_controller(id_gasto_comun, estado_pago):
        return GastoComunService.marcar_pago(id_gasto_comun, estado_pago)

    @staticmethod
    def obtener_pago_controller(id_gasto_comun):
        return GastoComunService.obtener_pago(id_gasto_comun)