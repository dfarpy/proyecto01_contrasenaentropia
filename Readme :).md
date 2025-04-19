🔐 Generador de Contraseñas Nivel Militar con Cálculo de Entropía

Este script fue desarrollado en Kali Linux como parte de un proyecto de ciberseguridad. Su objetivo es generar contraseñas altamente seguras mediante la incorporación de un nivel de entropía que cumple con estándares militares y buenas prácticas criptográficas.

🧠 ¿Qué es la Entropía en Contraseñas?

En términos científicos, la **entropía** mide el nivel de **incertidumbre o aleatoriedad** de un sistema. En el contexto de las contraseñas, se refiere a **cuán difícil es predecir o adivinar una contraseña**.

📊 Cálculo de entropía:

Se calcula usando la fórmula:

Entropía (bits) = log₂(N^L) = L × log₂(N)

Donde:
- `L` es la longitud de la contraseña.
- `N` es el número de posibles símbolos (por ejemplo, 26 letras minúsculas, 26 mayúsculas, 10 dígitos, y símbolos especiales).

📌 Ejemplo:
Una contraseña de 12 caracteres usando letras mayúsculas, minúsculas, números y símbolos tiene un espacio de 94 posibles caracteres (`N = 94`):

Entropía = 12 × log₂(94) ≈ 12 × 6.5546 ≈ 78.66 bits

Eso significa que una contraseña así tendría que ser adivinada entre **2⁷⁸** combinaciones, lo cual es computacionalmente inviable para ataques de fuerza bruta.

> ⚠️ Contraseñas con menos de **60 bits de entropía** se consideran débiles para estándares militares o gubernamentales.

🛠️ ¿Qué hace el script?

- Genera contraseñas aleatorias de longitud configurable.
- Permite incluir letras (mayúsculas y minúsculas), números y símbolos especiales.
- Calcula y muestra la entropía de la contraseña generada.
- Funciona completamente en terminal Linux.

📦 Requisitos

- Bash o cualquier shell compatible
- `tr`, `openssl` o `urandom` (dependiendo de la versión)
- Kali Linux (probado)
🚀 Uso

```bash
bash generador_contrasenas.sh

