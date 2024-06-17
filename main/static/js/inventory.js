document.addEventListener('DOMContentLoaded', function() {
	const selectElements = document.querySelectorAll('select');

	selectElements.forEach(selectElement => {
		selectElement.classList.add('select_search');
		selectElement.classList.add('form-select');
	});
});

$(document).ready(function() {
    $('.select_search').select2({
		language: "ja" //日本語化
	});

    for (let i = 0; i < 17; i++) {
        $('#id_inventory_id-' + i + '-is_out').blur(calc_invoice);
        $('#id_inventory_id-' + i + '-count').blur(calc_invoice);
        $('#id_inventory_id-' + i + '-price').blur(calc_invoice);
    }
    calc_invoice();

	const inputElements = document.querySelectorAll('input[type="text"], input[type="number"], input[type="date"]');
	inputElements.forEach(inputElement => {
		inputElement.classList.add('form-control');
	});

	const ths = document.querySelectorAll('th');
	ths.forEach(th => {
		th.classList.add('text-nowrap');
	});
});

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
 * 金額計算
 * @param {*} obj 
 */
function autoSum(obj) {
	obj.order_cost_price.value = Number(obj.order_price.value) + Number(obj.order_trans_cost.value) + Number(obj.parts_cost.value) + Number(obj.maintenance_cost.value) + Number(obj.order_out_order_cost.value);
	obj.sell_cost_price.value = Number(obj.sell_trance_cost.value) + Number(obj.ship_cost.value) + Number(obj.sell_out_order_cost.value) + Number(obj.ins_cost.value) + Number(obj.freight_cost.value) + Number(obj.order_cost_price.value);
	obj.profit.value = Number(obj.sell_price.value) - Number(obj.sell_cost_price.value);
}

/**
 * 請求金額計算する
 */
function calc_invoice() {
    // 明細行の金額算出と足しこみ
    for (let i = 0; i < 17; i++) {
        // 請求書出力対象かどうかチェック
        if (!$('#id_inventory_id-' + i + '-is_out').prop("checked")) continue;
        const row_total = Number($('#id_inventory_id-' + i + '-count').val()) * Number($('#id_inventory_id-' + i + '-price').val());
        $('#id_inventory_id-' + i + '-total').val(row_total);
    }
}