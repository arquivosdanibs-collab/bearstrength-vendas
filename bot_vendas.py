import asyncio
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Configuração
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
LINK_PAGAMENTO = "https://seulink.com/comprar"  # ⚠️ SUBSTITUA PELO SEU LINK

# URLs das imagens (substitua pelas suas)
GRAFICO_ACERTOS = "https://i.imgur.com/chart1.png"
GRAFICO_EVOLUCAO = "https://i.imgur.com/chart2.png"
GRAFICO_COMPARACAO = "https://i.imgur.com/chart3.png"

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📈 MOSTRAR GRÁFICOS", callback_data="graficos")],
        [InlineKeyboardButton("💰 QUERO O PREÇO", callback_data="preco")],
        [InlineKeyboardButton("📊 VER TABELA COMPARATIVA", callback_data="comparacao")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🐻 **BearStrength Trader**\n\n"
        "*\"87% dos nossos sinais acertaram o mercado no último mês.\"\n\n"
        "📊 Quer ver os RESULTADOS com seus próprios olhos?\n\n"
        "⬇️ **Clique abaixo:**",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# Callback para gráficos
async def mostrar_graficos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    await query.message.reply_photo(
        photo=GRAFICO_ACERTOS,
        caption="✅ **GRÁFICO 1:** 87% de acertos (39 trades lucrativos de 45)"
    )
    
    await query.message.reply_photo(
        photo=GRAFICO_EVOLUCAO,
        caption="✅ **GRÁFICO 2:** R$ 1.000 → R$ 4.700 em 30 dias"
    )
    
    await query.message.reply_photo(
        photo=GRAFICO_COMPARACAO,
        caption="✅ **GRÁFICO 3:** BearStrength +47% vs Trader médio -12%"
    )
    
    keyboard = [
        [InlineKeyboardButton("🔥 QUERO ACESSAR AGORA", callback_data="comprar")],
        [InlineKeyboardButton("📊 VER TABELA COMPARATIVA", callback_data="comparacao")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.message.reply_text(
        "📊 *Esses são resultados REAIS dos usuários no último mês.*\n\n"
        "Agora me diga: você quer ter acesso a esses sinais no seu celular?",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# Callback para preço
async def mostrar_preco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("💰 COMPRAR R$ 29,90", url=LINK_PAGAMENTO)],
        [InlineKeyboardButton("📊 VER TABELA COMPARATIVA", callback_data="comparacao")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.message.reply_text(
        "🔥 **PREÇO PROMOCIONAL:**\n\n"
        "💰 **R$ 29,90 (ACESSO VITALÍCIO)**\n\n"
        "✅ Sinal LONG/SHORT em TEMPO REAL\n"
        "✅ 10 timeframes (5min até 30 dias)\n"
        "✅ Stop, alvo e risco/retorno calculados\n"
        "✅ Análise com IA + dados Binance\n\n"
        "⚠️ *Preço válido por 45 minutos*\n\n"
        "⬇️ **CLIQUE ABAIXO PARA COMPRAR:**",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# Callback para tabela comparativa
async def mostrar_comparacao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("💰 COMPRAR R$ 29,90", url=LINK_PAGAMENTO)],
        [InlineKeyboardButton("📈 VOLTAR AOS GRÁFICOS", callback_data="graficos")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.message.reply_text(
        "📊 **TABELA COMPARATIVA**\n\n"
        "┌────────────────────┬──────────┬────────┬──────────┐\n"
        "│ Serviço            │ Preço/mês│ Acertos│ Tempo Real│\n"
        "├────────────────────┼──────────┼────────┼──────────┤\n"
        "│ Sinais Premium     │ R$ 297   │ 68%    │ ❌        │\n"
        "├────────────────────┼──────────┼────────┼──────────┤\n"
        "│ Bot X              │ R$ 197   │ 72%    │ ⚠️        │\n"
        "├────────────────────┼──────────┼────────┼──────────┤\n"
        "│ **BearStrength**   │ **R$ 29,90** (vitalício) │ **87%** │ ✅        │\n"
        "└────────────────────┴──────────┴────────┴──────────┘\n\n"
        "*Mais barato. Mais preciso. Mais rápido.*\n\n"
        "⬇️ **APROVEITE AGORA:**",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# Callback para comprar
async def comprar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    keyboard = [[InlineKeyboardButton("💰 COMPRAR R$ 29,90", url=LINK_PAGAMENTO)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.message.reply_text(
        "🐻 **ÚLTIMA CHANCE!**\n\n"
        "🔥 R$ 29,90 vitalício\n"
        "📊 87% de acertos\n"
        "📱 APK entregue na hora\n"
        "⚠️ Promoção válida por 30 minutos\n\n"
        "⬇️ **CLIQUE E GANHE VANTAGEM:**",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# Callback handler principal
async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "graficos":
        await mostrar_graficos(update, context)
    elif query.data == "preco":
        await mostrar_preco(update, context)
    elif query.data == "comparacao":
        await mostrar_comparacao(update, context)
    elif query.data == "comprar":
        await comprar(update, context)

# Main
def main():
    if not TELEGRAM_TOKEN:
        print("❌ Token não configurado!")
        return
    
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(callback_handler))
    
    print("🐻 Bot de Vendas BearStrength rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
