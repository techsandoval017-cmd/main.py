-- TABLA DE CLIENTES B2B
CREATE TABLE IF NOT EXISTS clientes_b2b (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    nombre_empresa VARCHAR(255) NOT NULL,
    correo_corporativo VARCHAR(255) UNIQUE NOT NULL,
    plan_suscripción VARCHAR(50) DEFAULT 'BASIC',
    estatus_pago VARCHAR(50) DEFAULT 'PENDIENTE'
);

-- TABLA DE INVENTARIO CRÍTICO
CREATE TABLE IF NOT EXISTS inventario_shopify (
    id_producto VARCHAR(100) PRIMARY KEY,
    nombre_articulo VARCHAR(255) NOT NULL,
    stock_actual INT NOT NULL,
    alerta_disparada BOOLEAN DEFAULT FALSE
);
