// ロード時にイベントハンドラを仕掛ける
$(document).ready(function(){
    for (let i = 0; i < 17; i++) {
        $('#id_work_id-' + i + '-count').blur(calc);
        $('#id_work_id-' + i + '-price').blur(calc);
    }
    $('#id_adjust').blur(calc);
});

/**
 * 計算する
 */
function calc() {
    // 明細行の金額算出と足しこみ
    let g_total = 0;
    for (let i = 0; i < 17; i++) {
        const row_total = 
            Number($('#id_work_id-' + i + '-count').val()) * Number($('#id_work_id-' + i + '-price').val());
        g_total = g_total + row_total;
        $('#id_work_id-' + i + '-total').val(row_total);
    }
    $('#id_sum').val(g_total);
    // 最終的な金額を算出する
    $('#id_total').val(
        Math.round((Number($('#id_sum').val()) + Number($('#id_adjust').val())) * 1.1)
    );
}