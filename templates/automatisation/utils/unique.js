// Suffixe unique pour les données créées par les tests (évite les collisions et
// permet de reconnaître les données de test dans l'environnement).
function uniqueSuffix() {
  return `${Date.now().toString(36)}${Math.random().toString(36).slice(2, 6)}`;
}

function qaLabel(base) {
  return `QA ${base} ${uniqueSuffix()}`;
}

module.exports = { uniqueSuffix, qaLabel };
