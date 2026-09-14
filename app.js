function sumar(a, b) {
  return a + b;
}

const resultado = sumar(5, 3);
console.log(`La suma de 5 + 3 = ${resultado}`);

// Información del sistema
const sistema = {
  nodeVersion: process.version.slice(1),
  plataforma: process.platform,
  arquitectura: process.arch,
  ultimaSuma: resultado
};

console.log(`
╔══════════════════════════════════════════════════╗
║           INFORMACIÓN DEL SISTEMA                ║
╚══════════════════════════════════════════════════╝

  Node.js:        v${sistema.nodeVersion}
  Plataforma:     ${sistema.plataforma}
  Arquitectura:   ${sistema.arquitectura}

  Original:       nardev
  Copia:          otra persona                »

  Última Suma:     ${sistema.ultimaSuma}

╔══════════════════════════════════════════════════╗
║   ® Todo funcionó! Tu versión de Node soporta    ║
║     estas funciones.                             ║
╚══════════════════════════════════════════════════╝
`);
