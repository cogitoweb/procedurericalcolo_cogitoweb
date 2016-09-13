openerp.library_module = function(instance, local) {
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;

    local.piano_dei_conti = instance.Widget.extend({
        start: function() {
            template: "PianoDeiConti",
            this.$el.append(QWeb.render("PianoDeiConti"));
            
        },
    });
    
    instance.web.client_actions.add('piano.conti', 'instances.library_module.piano_dei_conti');         
}
