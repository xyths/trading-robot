var preSumBalance = 0
var initSumBalance = 0
function UpdateAccount(isFirst){
    var msg = ""
    var sumStocks = 0
    var sumBalance = 0
    for(var i = 0; i < exchanges.length; i++){
        if(exchanges[i].needUpdate == true || isFirst == true){
            exchanges[i].account = _C(exchanges[i].GetAccount)
            exchanges[i].needUpdate = false
            if(isFirst == true){
                initSumBalance += (exchanges[i].account.Balance + exchanges[i].account.FrozenBalance)
                exchanges[i].SetPrecision(_CurrencyPrecision, _BaseCurrencyPrecision)
            }
        }
        sumStocks += (exchanges[i].account.Stocks + exchanges[i].account.FrozenStocks)
        sumBalance += (exchanges[i].account.Balance + exchanges[i].account.FrozenBalance)
        msg += exchanges[i].GetName() + "币:" + exchanges[i].account.Stocks + "冻币:" + exchanges[i].account.FrozenStocks + "钱:" + exchanges[i].account.Balance + "冻钱:" + exchanges[i].account.FrozenBalance + "\n"
    }
    LogStatus(_D(), "总币：" + sumStocks, "总钱：" + sumBalance, "\n", msg)
    if(preSumBalance != sumBalance){
        LogProfit(sumBalance - initSumBalance, preSumBalance = sumBalance)
    }
}
function main(){
    UpdateAccount(true)
    while(1){
        for(var i = 0; i < exchanges.length; i++){
            for(var j = 0; j < exchanges.length; j++){
                if(i == 0 && j == 0){
                    for(var m = 0; m < exchanges.length; m++){
                        exchanges[m].thread = exchanges[m].Go("GetTicker")
                    }
                    for(var n = 0; n < exchanges.length; n++){
                        exchanges[n].ticker = exchanges[n].thread.wait()
                    }
                }
                if(exchanges[i].GetName() != exchanges[j].GetName() && exchanges[i].ticker && exchanges[j].ticker && exchanges[i].ticker.Buy - exchanges[j].ticker.Sell > _HedgePrice){
                    if(exchanges[i].account.Stocks > _HedgeAmount && exchanges[j].account.Balance / ((exchanges[i].ticker.Buy + exchanges[j].ticker.Sell) / 2) > _HedgeAmount){
                        var sellId_I = exchanges[i].Sell((exchanges[i].ticker.Buy + exchanges[j].ticker.Sell) / 2, _HedgeAmount, exchanges[i].GetName())
                        var buyId_J = exchanges[j].Buy((exchanges[i].ticker.Buy + exchanges[j].ticker.Sell) / 2, _HedgeAmount, exchanges[i].GetName())
                        exchanges[i].needUpdate = exchanges[j].needUpdate = true
                    }
                }
            }
        }
        UpdateAccount(false)
        Sleep(300)      // 测试
    }
}