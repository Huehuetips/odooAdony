// odoo.define('your_module_name.disable_autosave', function (require) {
//     "use strict";

//     var FormView = require('web.FormView');

//     FormView.include({
//         _onSave: function (ev) {
//             // Evitar el guardado automático
//             ev.preventDefault();
//         },
//     });
// });