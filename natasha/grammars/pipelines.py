# coding: utf-8
from __future__ import unicode_literals

import os

from yargy.pipeline import CustomGrammemesPipeline

DICTIONARY_DIRECTORY = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'dictionaries',
)


class CommercialOrganisationPipeline(CustomGrammemesPipeline):

    Grammemes = {
        'Orgn/Commercial',
    }
    Dictionary = {
        'агентство',
        'компания',
        'организация',
        'издание',
        'интернет-издание',
        'издательство',
        'информационный_агентство',
        'информагентство',
        'газета',
        'концерн',
        'фирма',
        'завод',
        'торговый_дом',
        'предприятие',
        'корпорация',
        'группа',
        'группа_компания',
        'санаторий',
        'производственный_объединение',
        'совет_директор',
        'бюро',
        'подразделение',
        'филиал',
        'представительство',
        'издательский_дом',
        'ф-л',
        'банк',
        'биржа',
        'бар',
        'ресторан',
        'клуб',
        'рынок',
        'разработчик',
        'девелопер',
        'телеканал',
    }
    Path = os.path.join(DICTIONARY_DIRECTORY, 'orgn_commercial.dawg')


class SocialOrganisationPipeline(CustomGrammemesPipeline):

    Grammemes = {
        'Orgn/Social',
    }
    Dictionary = {
        'оргкомитет',
        'пресс-служба',
        'подразделение',
        'комитет',
        'редакция',
        'храм',
        'центр',
    
        'альянс',
        'союз',
        'совет',
        'служба',
        'театр',
        'музей',
        'общество',
        'объединение',
        'организация',

        'ассамблея',
        'министерство',
        'правительство',
        'руководство',
        'администрация',
        'кабинет_министр',
        'главный_управление',
        'управление',
        'союзный_государство',

        'больница',
        'госпиталь',
        'клиника',

        'дума',
        'госдума',
        'госдепартамент',
        'конгресс',
        'партия',
        'минздрав',

        'группировка',
        'фонд',
    }
    Path = os.path.join(DICTIONARY_DIRECTORY, 'orgn_social.dawg')


class EducationalOrganisationPipeline(CustomGrammemesPipeline):

    Grammemes = {
        'Orgn/Educational',
    }
    Dictionary = {
        'нии',
        'академия',
        'академия_наука',
        'обсерватория',
        'университет',
        'институт',
        'политех',
        'колледж',
        'техникум',
        'училище',
        'школа',
    }
    Path = os.path.join(DICTIONARY_DIRECTORY, 'orgn_educational.dawg')


class AbbreviationalOrganisationPipeline(CustomGrammemesPipeline):

    Grammemes = {
        'Orgn/Abbr',
    }
    Dictionary = {
        'ооо',
        'зао',
        'оао',
        'ао',
        'тоо',
        'фгуп',
        'пао',
        'уфпс',
        'нпо',
        'гк',
    }
    Path = os.path.join(DICTIONARY_DIRECTORY, 'orgn_abbr.dawg')

class PersonPositionPipeline(CustomGrammemesPipeline):

    Grammemes = {
        'Person/Position',
    }
    Dictionary = {
        'святой',
        'патриарх',
        'митрополит',

        'царь',
        'король',
        'царица',
        'император',
        'императрица',
        'принц',
        'принцесса',
        'князь',
        'граф',
        'графиня',
        'барон',
        'баронесса',
        'княгиня',

        'президент',
        'премьер-министр',
        'экс-премьер',
        'пресс-секретарь',
        'министр',
        'замминистр',
        'заместитель',
        'глава',
        'канцлер',
        'помощник',
        'посол',
        'губернатор',
        'председатель',
        'спикер',
        'диктатор',
        'лидер',
        'генсек',
        'премьер',
        'депутат',
        'вице-премьер',
        'сенатор',
        'полпред',
        'госсекретарь',
        'вице-президент',
        'сопредседатель',
        'зам',
        'мэр',
        'вице-спикер',
        'замруководителя',
        'зампред',
        'муфтий',
        'спецпредставитель',
        'руководитель',
        'статс-секретарь',
        'зампредседатель',
        'представитель',
        'ставленник',
        'мадеро',
        'вице-губернатор',
        'зампредсовмин',
        'наркоминдела',
        'генпрокурор',
        'комиссар',
        'рейхсканцлер',
        'советник',
        'замглавы',
        'секретарь',
        'парламентарий',
        'замгендиректор',
        'вице-председатель',
        'постпред',
        'госкомтруд',
        'предсовмин',
        'преемник',
        'делегат',
        'шеф',
        'консул',
        'замминистра',
        'главкомпис',
        'чиновник',
        'врио',
        'управделами',
        'нарком',
        'донпродкомиссар',
        'председ',
        'гендиректор',
        'генерал-губернатор',
        'обревком',
        'правитель',
        'замсекретарь',
        'главнокомандующий',
        'вице-мэр',
        'председательство',
        'наместник',
        'спичрайтер',
        'вице-консул',
        'мвэс',
        'облревком',
        'главковерх',
        'пресс-атташе',
        'торгпред',
        'член',
        'назначенец',
        'эмиссар',
        'обрядоначальник',
        'главком',
        'единоросс',
        'политик',
        'генерал',
        'замгенпрокурор',
        'дипломат',
        'главноуполномоченный',
        'генерал-фельдцейхмейстер',
        'комендант',
        'казначей',
        'уполномоченный',
        'обер-прокурор',
        'еврокомиссия',
        'наркомзем',
        'соправитель',

        'основатель',
        'сооснователь',
        'управляющий_директор',
        'управляющий_партнер',
        'партнер',
        'руководитель',
        'аналитик',
        'зампред',
        'миллиардер',
        'миллионер',

        'автор',
        'актер',
        'актриса',
        'артист',
        'певец',
        'певица',
        'исполнитель',
        'солист',
        'режиссер',
        'сценарист',
        'писатель',
        'музыкант',
        'композитор',
        'корреспондент',
        'журналист',
        'редактор',
        'дирижер',
        'кинорежиссер',
        'звукорежиссер',
        'детектив',
        'пианист',
        'драматург',
        'художник',
        'артистка',
        'балетмейстер',
        'скрипач',
        'хореограф',
        'танцовщик',
        'документалист',
        'поэт',
        'литератор',
        'киноактер',
        'вокалист',
        'бард',
        'комик',
        'продюсер',
        'кинодраматург',
        'киноактриса',
        'балерина',
        'пианистка',
        'критик',
        'танцор',
        'концертмейстер',
        'симфонист',
        'сатирик',
        'аранжировщик',
        'саксофонист',
        'юморист',
        'шансонье',
        'гастролер',
        'виолончелист',
        'постановщик',
        'кинематографист',
        'сценограф',
        'джазмен',
        'музыковед',
        'киноартист',
        'педагог',
        'хормейстер',
        'беллетрист',
        'примадонна',
        'инструменталист',
        'альтист',
        'шоумен',
        'виртуоз',
        'пародист',
        'декоратор',
        'модельер',
        'очеркист',
        'оперетта',
        'контрабасист',
        'карикатурист',
        'дуэт',
        'монтажер',
        'живописец',
        'скульптор',
        'режиссура',
        'архитектор',
        'антрепренер',
        'импрессарио',
        'прозаик',
        'труппа',
        'трагик',
        'клоун',
        'солистка',
        'либреттист',
        'литературовед',
        'портретист',
        'гример',
        'художница',
        'импровизатор',
        'декламаторша',
        'телеведущий',
        'импресарио',
        'мастер',
        'аккомпаниатор',
        'шахматист',
        'иллюзионист',
        'эстрадник',
        'эстрада',
        'спортсмен',
        'дизайнер',
        'кинокритик',
        'публицист',
        'чтец',
        'конферансье',
        'студиец',
        'коверный',
        'куплетист',
        'знаменитость',
        'ученый',
        'балет',
        'искусствовед',
        'гитарист',

        'доктор',

        'академик',

        'судья',
        'юрист',
        'представитель',
        'директор',
        'прокурор',

        'отец',
        'мать',
        'мама',
        'папа',
        'брат',
        'сестра',
        'тёща',
        'тесть',
        'дедушка',
        'бабушка',
        'жена',
        'муж',
        'дочь',
        'сын',

        'мистер',
        'миссис',
        'господин',
        'госпожа',
        'пан',
        'пани',
        'сэр',
        'мисс',

        'боксер',
        'боец',
        'атлет',
        'футболист',
        'баскетболист',

        'агроном',
    }

    Path = os.path.join(DICTIONARY_DIRECTORY, 'person_position.dawg')
