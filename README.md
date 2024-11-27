# AI GEKKO
##### ![](https://github.com/arnaldoquinones/henry_ai/blob/master/media/ia_gekko.png?raw=true)

# Descripcion del proyecto.

Desarrollaremos una plataforma web financiera diseñada para centralizar toda la información relevante a la gestión del usuario en un único sitio. Esta herramienta integrará un sistema de inteligencia artificial que ofrecerá tanto actualizaciones en tiempo real como proyecciones sobre activos financieros. 
La plataforma también incluirá análisis de tendencias de activos, evaluación de estados contables y generación de reportes económico-financieros. Además, mediante técnicas de web scraping, proporcionará información clave que facilitará la toma de decisiones.


# Pipeline y Stack Tecnológico.

Para implementar el proyecto, se utilizarán las siguientes tecnologías y herramientas:

- **Python**: Herramientas y bibliotecas como Pandas, Numpy, Matplotlib y Seaborn serán utilizadas para la manipulación, análisis y visualización de datos.
- **Reflex.** 
- **Visualización.**
- **Modelos de Machine Learning.**

# APIs.
A modo ilustrativo se provee de una lista de las principales APIs que se emplearan en el proyecto:

- **CHATGPT.**
- **BCRA.**
- **YAHOO FINANCIAL.**
- **AMBITO FINANCIERO.**
- **CRONISTA COMERCIAL.**
- **WALL STREET JOURNAL.**
- **REALTIME NEWS APIS.**

# Workflow.

Sprint 1: Definición y Configuración
	Objetivo: Establecer las bases del proyecto, definir la arquitectura y configurar el entorno.

	Tareas principales:

	1) Definición del alcance:
		Identificar usuarios y roles: básico, analista, administrador.
		Definir las funcionalidades principales (noticias, indicadores, correlaciones).
	2) Diseño de la arquitectura:
		Dividir en módulos: autenticación, APIs, scraping, vistas dinámicas.
		Crear diagramas de flujo para los procesos clave.
	3) Configuración del entorno:
		Crear el entorno virtual con Python y Reflex.
		Configurar control de versiones con Git/GitHub.
	4) Prototipo inicial de UI:
		Usar Reflex para diseñar pantallas preliminares (login, dashboard).
	Entregables:

		Requerimientos documentados y arquitectura definida.
		Entorno de desarrollo configurado.
		Prototipo básico de interfaz.

-------------------------------------------------------------------------------------------------------------------
Sprint 2: Implementación de la Autenticación y Perfiles
	Objetivo: Implementar el sistema de inicio de sesión y gestionar perfiles de usuarios.

	Tareas principales:

	1) Autenticación:
		Crear sistema de login con validación (ej.: correo y contraseña).
		Configurar la base de datos para almacenar credenciales y perfiles.
	2) Roles de usuario:
		Definir permisos y vistas específicas según el rol (básico, analista, administrador).
		Probar restricciones en las funcionalidades.
	3) Página de inicio personalizada:
		Mostrar contenido inicial según el perfil del usuario.
		Diseñar menús adaptativos para cada rol.
	Entregables:

		Sistema de autenticación funcional.
		Gestión de roles implementada.
		Inicio de sesión personalizado para cada tipo de usuario.

-------------------------------------------------------------------------------------------------------------------
Sprint 3: Integración con APIs y Web Scraping
	Objetivo: Conectar la aplicación con APIs externas y habilitar la recopilación de noticias.

	Tareas principales:

	1) APIs financieras:
		Integrar una API para obtener datos financieros (ej.: Yahoo Finance, Alpha Vantage).
		Mostrar indicadores básicos (ej.: precios, volúmenes).
	2) API de IA:
		Conectar la API de OpenAI para generar resúmenes y análisis automatizados.
	3) Web scraping:
		Configurar scraping de noticias relevantes usando BeautifulSoup o Scrapy.
		Procesar y limpiar los datos obtenidos.
	4) Visualización inicial:
		Diseñar componentes para mostrar noticias e indicadores en el dashboard.
	Entregables:

		Integración con APIs funcionando.
		Sistema de web scraping funcional.
		Vista inicial con noticias e indicadores.

-------------------------------------------------------------------------------------------------------------------
Sprint 4: Análisis Avanzado y Visualización
	Objetivo: Implementar correlaciones, análisis de datos y gráficos interactivos.

	Tareas principales:

	1) Análisis de datos:
		Calcular correlaciones entre indicadores financieros y mostrar resultados.
		Generar análisis automáticos con ayuda de IA.
	2) Visualización avanzada:
		Crear gráficos interactivos usando Plotly o Dash.
		Diseñar vistas con filtros dinámicos (por fecha, sector, región).
	3) Optimización del scraping:
		Mejorar el rendimiento y la actualización de noticias.
		Implementar alertas o actualizaciones automáticas en el sistema.
	4) Pruebas funcionales:
		Validar exactitud y rendimiento de las vistas y cálculos.
	Entregables:

		Correlaciones y análisis avanzados implementados.
		Gráficos interactivos funcionales.
		Sistema probado y optimizado.

--------------------------------------------------------------------------------------------------------------------
Sprint 5: Refinamiento, Seguridad y Despliegue
	Objetivo: Optimizar la aplicación, garantizar seguridad y preparar el despliegue.

	Tareas principales:

	1) Optimización del sistema:
		Mejorar tiempos de carga y eficiencia del backend.
		Usar caché para datos que no cambian frecuentemente.
	2) Seguridad:
		Implementar medidas de seguridad en el login y las APIs.
		Validar entradas del usuario para prevenir ataques (ej.: inyección SQL, XSS).
	3) Documentación:
		Escribir documentación técnica para desarrolladores.
		Crear una guía para usuarios finales.
	4) Despliegue:
		Configurar despliegue en un servidor en la nube (ej.: Heroku, AWS, DigitalOcean).
		Realizar pruebas finales en el entorno de producción.
	Entregables:

		Sistema optimizado y seguro.
		Documentación lista.
		Aplicación desplegada y lista para el usuario.

# Disclaimer legal.

A fin de darle la impronta profesional que un proyecto de esta envergadura demanda se destinara un area de la plataforma con un disclaimer legal dejando en claro que la misma ofrece informacion para la toma de decisiones y que, bajo ningun concepto otorga consejos sobre inversiones a realizar. 

"...El contenido presentado en AI_GEKKO tiene fines estrictamente informativos y educativos. La información proporcionada, incluyendo análisis, actualizaciones en tiempo real, proyecciones, reportes y evaluaciones financieras, está diseñada para asistir al usuario en la gestión y organización de sus decisiones financieras. 
**AI_GEKKO no constituye una asesoría financiera profesional ni ofrece recomendaciones de inversión.** Bajo ningún concepto, las herramientas, reportes o análisis generados por la plataforma deben interpretarse como consejos específicos de inversión, estrategias personalizadas, o una garantía de rendimiento financiero.
Se aconseja a los usuarios que consulten a un asesor financiero profesional antes de tomar cualquier decisión de inversión, ya que los mercados financieros implican riesgos significativos. AI_GEKKO no se responsabiliza por decisiones tomadas con base en la información proporcionada por la plataforma, ni por pérdidas o daños derivados de dichas decisiones.
Al utilizar AI_GEKKO, los usuarios aceptan estos términos y reconocen que la plataforma es una herramienta de apoyo informativo, no un sustituto de asesoramiento financiero profesional..."

# Team staff.

- Federico Mamani  | Data engineer.
- Santiago Ratto   | Data scientist.
- Arnaldo Quiñones | Data Analist/fullstack developer.




