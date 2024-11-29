/** @odoo-module */
import { FormController } from "@web/views/form/form_controller";
import { patch } from "@web/core/utils/patch";
import { useSetupView } from "@web/views/view_hook";

patch(FormController.prototype, {
    setup() {
        super.setup(...arguments);
        // Solo aplica para el modelo específico
        if (this.props.resModel === 'tracking_guide.history_guide') {
            useSetupView({
                beforeLeave: () => this.beforeLeave(),
            });
        }
    },
    async beforeLeave() {
        if (this.props.resModel === 'tracking_guide.history_guide' && this.model.root.isDirty) {
                this.model.root.discard();
        }else{
            this.model.root.save({
                reload: false,
                onError: this.onSaveError.bind(this),
            });
            // window.location.reload();
        }
    }
});
