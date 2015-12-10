cur_frm.add_fetch('produto', 'produto', 'descricao');
cur_frm.add_fetch('produto', 'preco_de_venda', 'preco_de_venda');

cur_frm.cscript.calcular_subtotal = function(d){
	if (d && d.quantidade && d.preco_de_venda) {
		frappe.model.set_value(d.doctype, d.name, 'subtotal', d.quantidade * d.preco_de_venda);
	}
}

cur_frm.cscript.calcular_total = function(doc){
	var total = 0;
	doc.itens.forEach(function(d){
		total += d.subtotal;
	});
	frappe.model.set_value(doc.doctype, doc.name, 'total', total);
	cur_frm.refresh_field('total');
}

frappe.ui.form.on('Venda Itens', 'quantidade', function(frm, cdt, cdn){
	frm.cscript.calcular_subtotal(locals[cdt][cdn]);
	frm.cscript.calcular_total(frm.doc);
});

frappe.ui.form.on('Venda Itens', 'preco_de_venda', function(frm, cdt, cdn){
	frm.cscript.calcular_subtotal(locals[cdt][cdn]);
	frm.cscript.calcular_total(frm.doc);
});
