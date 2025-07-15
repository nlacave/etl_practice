// Ejercicio 2 – Simulación y análisis de un dataLayer en el navegador

// Paso 1: Inicializar el dataLayer (estructura tipo array)
window.dataLayer = window.dataLayer || [];

// Paso 2: Pushear un objeto de evento de compra al dataLayer
// Incluir: transaction_id, value, currency, y un array de productos con id, name, y price

// TU CÓDIGO AQUÍ 👇


// Paso 3: Desde la consola del navegador:
// - Mostrar el valor total de la compra
// - Mostrar el nombre del primer producto
// - Obtener un array con todos los nombres de productos

// Sugerencia:
// console.log(dataLayer[0].ecommerce.value)
// console.log(dataLayer[0].ecommerce.items[0].name)
// console.log(dataLayer[0].ecommerce.items.map(item => item.name))
