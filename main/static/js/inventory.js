/**
 * 在庫検索
 */
function search() {
	document.forms[1].action = "/inventory/";
    document.forms[1].method = "GET";
	document.forms[1].submit();
}

/**
 * 在庫削除
 * @param {*} action 
 */
function deleteInventory(action) {
    if(!confirm("削除してよろしいでしょうか？")) {
        return;
    }
	document.forms[1].action = action;
    document.forms[1].method = "POST";
	document.forms[1].submit();
}

/**
 * 請求書発行
 */
function downloadJpinvoice() {
	document.forms[1].action = "/inventory/download_jpinvoice/";
    document.forms[1].method = "POST";
	document.forms[1].submit();
}

/**
 * Proforma Invoice発行
 */
function downloadProformaInvoice() {
	document.forms[1].action = "/inventory/download_proforma_invoice/";
    document.forms[1].method = "POST";
	document.forms[1].submit();
}

/**
 * 金額計算
 * @param {*} obj 
 */
function autoSum(obj) {
	obj.order_cost_price.value = Number(obj.order_price.value) + Number(obj.order_trans_cost.value) + Number(obj.parts_cost.value) + Number(obj.maintenance_cost.value) + Number(obj.order_out_order_cost.value);
	obj.sell_cost_price.value = Number(obj.sell_trance_cost.value) + Number(obj.ship_cost.value) + Number(obj.sell_out_order_cost.value) + Number(obj.ins_cost.value) + Number(obj.freight_cost.value) + Number(obj.order_cost_price.value);
	obj.profit.value = Number(obj.sell_price.value) - Number(obj.sell_cost_price.value);
}