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
