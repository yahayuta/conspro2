/**
 * 在庫削除
 * @param {*} action 
 * @returns 
 */
function deleteInventory(action) {
    if(!confirm("削除してよろしいでしょうか？")) {
        return;
    }
	document.forms[0].action = action;
    document.forms[0].method = "POST";
	document.forms[0].submit();
}