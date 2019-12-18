
import pickle
import sys

sys.path.append('../../Creating')
from CA_create import CognitiveAssistant, ScriptGraphVert
from CA_create import ScriptGraphVert as SCV


dict_vert = {}

vert = SCV(name = "start", 
        texts = ["Здравствуйте. Приступим к выбору автомобиля."],
        is_start = True)
dict_vert["start"] = vert

name = "Выбор"
vert = SCV(name = name, 
        texts = ["Выберите автомобиль.",
            "Определитесь с суммой покупки",
            "Обратите внимание на кузов, трансмиссию, производителя."])
dict_vert[name] = vert

name = "Осмотр"
vert = SCV(name = name,
        texts = [])
dict_vert[name] = vert

name = "Осмотр_бу"
vert = SCV(name = name,
        texts = ["Осмотрите деффекты лакокрсочного покрытия.",
            "Оцените возраст автомобиля по изношенности салона и уплотнителей.",
            "Прокатитесь на автомобиле."])
dict_vert[name] = vert

name = "Осмотр_новая"
vert = SCV(name = name,
        texts = ["Осмотрите представленные в салоне автомобиле. Оцените комфорт и соответствие желаниям",
            "Побеседуйте с консультантом. Распросите про возможные варианты, скидки и бонусы.",
            "Воспользуйтесь тест-драйвом при возможности.",
            "Проверьте условия договора. Убедитесь в соответствии всех пунктов  в документации."])
dict_vert[name] = vert

name = "Юридическая_Проверка_бу"
vert = SCV(name = name,
        texts = ["Спросите у продавца ВИН номер автомоболи и проверьте данные автомобиля на сайте ГИБДД."])
dict_vert[name] = vert

name = "Оформление_покупки"
vert = SCV(name = name,
        texts = [])
dict_vert[name] = vert

name = "Оформление_бу_частник"
vert = SCV(name = name,
        texts = ["Подпишите договор купли-продажи.",
            "Внесите изменения в ПТС.",
            "Получите ключи от Авто.",
            "Оформите ОСАГО.",
            "Зарегестируйте авто в ГИБДД."])
dict_vert[name] = vert

name = "Оформление_новая_БезКредита"
vert = SCV(name = name,
        texts = ["Автомобиль, как правило, приходится подождать. В таком случае нужно будет сделать заказ выбранной модели и, возможно, внести задаток.",
            "При доставке автомобиля проведите осмотр вновь.",
            "Подпишите договор купли-продажи. Перепрочтите его перед подписанием.",
            "Внесите полную стоимость авто и получите его.",
            "Оформите ОСАГО. Подумайте над КАСКО. ...Советы, различия...",
            "Зарегистрируйте авто в ГИБДД"])
dict_vert[name] = vert

name  = "Оформление_новая_кредит"
vert = SCV(name = name,
        texts = ["Выберете кредитную организацию, подайте документы и ждите одобрения.",
            "Выполните условия кредитного договора (напр., покупка КАСКО и внесение первого взноса)",
            "Подписание договора.",
            "Получите авто.",
            "Зарегистрируйте авто в ГИБДД",
            "Передайте ПТС банку, выдавшему кредит"])
dict_vert[name] = vert

dict_vert["end"] = SCV(name = "end", texts = ["Поздравляю с покупкой автомобиля."], is_terminal = True)

dict_vert["start"].add_edge(child = dict_vert["Выбор"], cond = "")
dict_vert['start'].add_edge(child = dict_vert["Осмотр"], cond = "Осмотр")
dict_vert["start"].add_edge(child = dict_vert["Оформление_покупки"], cond = "Оформление")
dict_vert['Выбор'].add_edge(child = dict_vert["Осмотр"], cond = "")
dict_vert["Осмотр"].add_edge(child = dict_vert["Осмотр_бу"], cond = "бу")
dict_vert["Осмотр"].add_edge(child = dict_vert["Осмотр_новая"], cond = "новая")
dict_vert["Осмотр_бу"].add_edge(child = dict_vert["Оформление_покупки"], cond = "")
dict_vert["Осмотр_новая"].add_edge(child = dict_vert["Оформление_покупки"], cond = "")
dict_vert["Оформление_покупки"].add_edge(child = dict_vert["Оформление_бу_частник"], cond = "бу_частник")
dict_vert["Оформление_покупки"].add_edge(child = dict_vert["Оформление_новая_БезКредита"], cond = "новая без кредита")
dict_vert["Оформление_покупки"].add_edge(child = dict_vert["Оформление_новая_кредит"], cond = "новая с кредитом")
dict_vert["Оформление_бу_частник"].add_edge(child = dict_vert["end"], cond = "")
dict_vert["Оформление_новая_БезКредита"].add_edge(child = dict_vert["end"], cond = "")
dict_vert["Оформление_новая_кредит"].add_edge(child = dict_vert["end"], cond = "")

CA = CognitiveAssistant("trivial", dict_vert["start"])
CA.dialogue_start()
with open("CA_trivial.pickle", "wb") as f:
    pickle.dump(CA, f)
    f.close()
