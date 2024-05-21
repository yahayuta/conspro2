document.addEventListener('DOMContentLoaded', function() {
	const selectElements = document.querySelectorAll('select');

	selectElements.forEach(selectElement => {
		selectElement.classList.add('select_search');
		selectElement.classList.add('form-select');
	});
});

// ロード時にイベントハンドラを仕掛ける
$(document).ready(function(){

    $('.select_search').select2({
		language: "ja" //日本語化
	});

    for (let i = 0; i < 17; i++) {
        $('#id_rental_order_id-' + i + '-is_out').blur(calc_invoice);
        $('#id_rental_order_id-' + i + '-count').blur(calc_invoice);
        $('#id_rental_order_id-' + i + '-price').blur(calc_invoice);
    }
    $('#id_adjust').blur(calc_invoice);

    calc_invoice();
});

/**
 * 請求金額計算する
 */
function calc_invoice() {
    // 明細行の金額算出と足しこみ
    let g_total = 0;
    for (let i = 0; i < 17; i++) {
        // 請求書出力対象かどうかチェック
        if (!$('#id_rental_order_id-' + i + '-is_out').prop("checked")) continue;
        const row_total = Number($('#id_rental_order_id-' + i + '-count').val()) * Number($('#id_rental_order_id-' + i + '-price').val());
        g_total = g_total + row_total;
        $('#id_rental_order_id-' + i + '-total').val(row_total);
    }
    $('#id_sum').val(g_total);
    // 最終的な金額を算出する
    $('#id_total').val(
        Math.round((Number($('#id_sum').val()) + Number($('#id_adjust').val())) * 1.1)
    );
}