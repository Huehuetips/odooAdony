// /** @odoo-module */
// import { FormController } from "@web/views/form/form_controller";
// import { patch } from "@web/core/utils/patch";
// import { useSetupView } from "@web/views/view_hook";

// patch(FormController.prototype, {
//     setup() {
//         super.setup(...arguments);
//         if (this.props.resModel === 'tracking_guide.history_guide') {
//             this.beforeLeaveHook = false;
//             useSetupView({
//                 beforeLeave: this.beforeLeave.bind(this),
//             });
//         }
//     },
//     async beforeLeave() {
//         if (this.props.resModel === 'tracking_guide.history_guide' && this.model.root.isDirty && !this.beforeLeaveHook) {
//             if (confirm("Realmente quieres salir sin guardar los cambios?")) {
//                 this.beforeLeaveHook = true;
//                 // this.model.root.discard();
//             } else {
//                 this.beforeLeaveHook = true;
//                 return false; // Evita que la página cambie
//             }
//         }
//     }
// });

odoo.define('tracking_guide.disable_autosave', ['web.FormController'], function (require) {
    "use strict";

    var FormController = require('web.FormController');

    FormController.include({
        saveRecord: function () {
            // Sobrescribe el método saveRecord para deshabilitar el guardado automático
            if (this.modelName === 'tracking_guide.history_guide') {
                console.log('Guardado automático deshabilitado para tracking_guide.history_guide');
                return Promise.resolve();
            }
            return this._super.apply(this, arguments);
        }
    });
});

console.log("Hola")