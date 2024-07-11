from django.db import models


class Bodega(models.Model):
    num_pasillo = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)

    class Meta:
        db_table = 'bodega'


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=30)

    class Meta:
        db_table = 'categoria'


class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=30)
    codigo_postal = models.IntegerField()
    region = models.ForeignKey('Region', on_delete=models.DO_NOTHING, db_column='region_id_region')

    class Meta:
        db_table = 'ciudad'


class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=40)
    apellido_paterno = models.CharField(max_length=40)
    apellido_materno = models.CharField(max_length=40)
    genero = models.CharField(max_length=1)
    telefono = models.IntegerField()
    email = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.DO_NOTHING, db_column='ciudad_id_ciudad')

    class Meta:
        db_table = 'cliente'


class CuentaCliente(models.Model):
    email = models.CharField(primary_key=True, max_length=40)
    clave = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, db_column='cliente_rut')

    class Meta:
        db_table = 'cuenta_cliente'


class CuentaEmpleado(models.Model):
    usuario = models.CharField(primary_key=True, max_length=20)
    clave = models.CharField(max_length=20)
    rol = models.ForeignKey('Rol', on_delete=models.DO_NOTHING, db_column='rol_id_rol')
    empleado = models.ForeignKey('Empleado', on_delete=models.DO_NOTHING, db_column='empleado_rut')

    class Meta:
        db_table = 'cuenta_empleado'


class DetalleOrden(models.Model):
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    cuenta_cliente = models.ForeignKey(CuentaCliente, on_delete=models.DO_NOTHING, db_column='cuenta_cliente_email')
    empleado = models.ForeignKey('Empleado', on_delete=models.DO_NOTHING, db_column='empleado_rut')
    producto = models.ForeignKey('Producto', on_delete=models.DO_NOTHING, db_column='producto_id_producto')

    class Meta:
        db_table = 'detalle_orden'


class Empleado(models.Model):
    rut = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    genero = models.CharField(max_length=1)
    telefono = models.IntegerField()
    email = models.CharField(max_length=30)
    cargo = models.IntegerField()

    class Meta:
        db_table = 'empleado'


class EstadoPago(models.Model):
    nombre_estado_pago = models.CharField(max_length=30)

    class Meta:
        db_table = 'estado_pago'


class EstadoPedido(models.Model):
    nombre_estado_pedido = models.CharField(max_length=30)

    class Meta:
        db_table = 'estado_pedido'


class Estanteria(models.Model):
    capacidad = models.IntegerField()
    pasillo = models.ForeignKey('Pasillo', on_delete=models.DO_NOTHING, db_column='pasillo_id_pasillo')
    producto = models.ForeignKey('Producto', on_delete=models.DO_NOTHING, db_column='producto_id_producto', blank=True, null=True)

    class Meta:
        db_table = 'estanteria'


class Marca(models.Model):
    nombre_marca = models.CharField(max_length=30)

    class Meta:
        db_table = 'marca'


class Oferta(models.Model):
    id_proveedor = models.IntegerField()
    nombre_proveedor = models.CharField(max_length=40)
    apellido_proveedor = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    oferta = models.CharField(max_length=300)
    fecha = models.DateField()
    empleado = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING, db_column='empleado_rut')

    class Meta:
        db_table = 'oferta'


class OrdenCompra(models.Model):
    precio_total = models.IntegerField()
    fecha_compra = models.DateField()
    fecha_estimada = models.DateField()
    estado_pago = models.ForeignKey(EstadoPago, on_delete=models.DO_NOTHING, db_column='estado_pago_id_estado_pago')
    detalle_orden = models.ForeignKey(DetalleOrden, on_delete=models.DO_NOTHING, db_column='detalle_orden_id_detalle_orden')
    estado_pedido = models.ForeignKey(EstadoPedido, on_delete=models.DO_NOTHING, db_column='estado_pedido_id_estado_pedido')
    tipo_pago = models.ForeignKey('TipoPago', on_delete=models.DO_NOTHING, db_column='tipo_pago_id_tipo_pago')
    tipo_orden = models.ForeignKey('TipoOrden', on_delete=models.DO_NOTHING, db_column='tipo_orden_id_tipo_orden')

    class Meta:
        db_table = 'orden_compra'


class Pasillo(models.Model):
    num_estanteria = models.IntegerField()
    bodega = models.ForeignKey(Bodega, on_delete=models.DO_NOTHING, db_column='bodega_id_bodega')

    class Meta:
        db_table = 'pasillo'


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField()
    oferta = models.CharField(max_length=1)
    porcentaje = models.IntegerField(blank=True, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING, db_column='marca_id_marca')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, db_column='categoria_id_categoria')

    class Meta:
        db_table = 'producto'


class Region(models.Model):
    nombre_region = models.CharField(max_length=30)

    class Meta:
        db_table = 'region'


class Rol(models.Model):
    nombre_rol = models.CharField(max_length=30)

    class Meta:
        db_table = 'rol'


class SolicitudPresencial(models.Model):
    id_producto = models.IntegerField()
    nombre_producto = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    orden_compra = models.OneToOneField(OrdenCompra, on_delete=models.DO_NOTHING, db_column='orden_compra_id_orden', primary_key=True)

    class Meta:
        db_table = 'solicitud_presencial'


class SolicitudProductos(models.Model):
    nombre_producto = models.CharField(max_length=30)
    nombre_categoria = models.IntegerField()
    precio = models.IntegerField()
    nombre_marca = models.IntegerField()
    stock = models.IntegerField()
    observacion = models.CharField(max_length=30, blank=True, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING, db_column='empleado_rut')

    class Meta:
        db_table = 'solicitud_productos'


class TipoOrden(models.Model):
    nombre_orden = models.CharField(max_length=30)

    class Meta:
        db_table = 'tipo_orden'


class TipoPago(models.Model):
    nombre_pago = models.CharField(max_length=30)

    class Meta:
        db_table = 'tipo_pago'


class Valoracion(models.Model):
    valoracion = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, db_column='producto_id_producto')

    class Meta:
        db_table = 'valoracion'