from enum import Enum

SHORT_VERSION = "0.0.12"
REV_VERSION = "2"
VERSION_DEV_PHASE = "alpha"
VERSION = "{0}-{1}".format(SHORT_VERSION, VERSION_DEV_PHASE)
LONG_VERSION = "{0}_{1}-{2}".format(SHORT_VERSION, REV_VERSION, VERSION_DEV_PHASE)

ORIGIN_URL = "https://github.com/Drakkar-Software/Octobot.git"

MSECONDS_TO_SECONDS = 1000
MINUTE_TO_SECONDS = 60
HOURS_TO_SECONDS = MINUTE_TO_SECONDS * 60
HOURS_TO_MSECONDS = MSECONDS_TO_SECONDS * MINUTE_TO_SECONDS * MINUTE_TO_SECONDS
DAYS_TO_SECONDS = HOURS_TO_SECONDS * 24

CONFIG_GLOBAL_UTILS = "global_utils"
CONFIG_ENABLED_OPTION = "enabled"
CONFIG_SYMBOL = "symbol"

# Files
CONFIG_FILE = "config/config.json"
CONFIG_EVALUATOR_FILE = "config/evaluator_config.json"

# Advanced
CONFIG_ADVANCED_CLASSES = "advanced_classes"
CONFIG_ADVANCED_INSTANCES = "advanced_instances"

# Backtesting
CONFIG_BACKTESTING = "backtesting"
CONFIG_BACKTESTING_DATA_FILES = "files"

# Data collector
CONFIG_DATA_COLLECTOR = "data_collector"
CONFIG_DATA_COLLECTOR_ZIPLINE = "zipline"
DATA_COLLECTOR_REFRESHER_TIME = MINUTE_TO_SECONDS
CONFIG_DATA_COLLECTOR_PATH = "backtesting/collector/data/"

# Trading
CONFIG_EXCHANGES = "exchanges"
CONFIG_EXCHANGE_WEB_SOCKET = "web_socket"
CONFIG_EXCHANGE_KEY = "api-key"
CONFIG_EXCHANGE_SECRET = "api-secret"
CONFIG_TRADER = "trader"
CONFIG_SIMULATOR = "trader_simulator"
CONFIG_STARTING_PORTFOLIO = "starting_portfolio"
CONFIG_TRADER_RISK = "risk"
CONFIG_TRADER_RISK_MIN = 0.05
CONFIG_TRADER_RISK_MAX = 1
ORDER_REFRESHER_TIME = 15
SIMULATOR_LAST_PRICES_TO_CHECK = 15
ORDER_CREATION_LAST_TRADES_TO_USE = 10
CONFIG_TRADER_REFERENCE_MARKET = "reference_market"
DEFAULT_REFERENCE_MARKET = "BTC"
MARKET_SEPARATOR = "/"
CURRENCY_DEFAULT_MAX_PRICE_DIGITS = 8

CONFIG_PORTFOLIO_INFO = "info"
CONFIG_PORTFOLIO_FREE = "free"
CONFIG_PORTFOLIO_USED = "used"
CONFIG_PORTFOLIO_TOTAL = "total"

# Notification
CONFIG_NOTIFICATION_INSTANCE = "notifier"
CONFIG_CATEGORY_NOTIFICATION = "notification"
NOTIFICATION_STARTING_MESSAGE = "Octobot v{0} starting...".format(LONG_VERSION)
NOTIFICATION_STOPPING_MESSAGE = "Octobot v{0} stopping...".format(LONG_VERSION)

# DEBUG options
CONFIG_DEBUG_OPTION_PERF = "performance_analyser"
CONFIG_DEBUG_OPTION_PERF_REFRESH_TIME_MIN = 5
CONFIG_DEBUG_OPTION = "DEBUG"

# SERVICES
CONFIG_CATEGORY_SERVICES = "services"
CONFIG_SERVICE_INSTANCE = "service_instance"

# gmail
CONFIG_GMAIL = "gmail"

# telegram
CONFIG_TELEGRAM = "telegram"
CONFIG_TOKEN = "token"

# web
CONFIG_WEB = "web"
CONFIG_WEB_IP = "ip"
CONFIG_WEB_PORT = "port"
DEFAULT_SERVER_IP = '0.0.0.0'
DEFAULT_SERVER_PORT = 5001

# twitter
CONFIG_TWITTERS_ACCOUNTS = "accounts"
CONFIG_TWITTERS_HASHTAGS = "hashtags"
CONFIG_TWITTER = "twitter"
CONFIG_REDDIT = "reddit"
CONFIG_REDDIT_SUBREDDITS = "subreddits"
CONFIG_REDDIT_ENTRY = "entry"
CONFIG_REDDIT_ENTRY_WEIGHT = "entry_weight"
CONFIG_TWITTER_API_INSTANCE = "twitter_api_instance"
CONFIG_TWEET = "tweet"
CONFIG_TWEET_DESCRIPTION = "tweet_description"

# Evaluator
CONFIG_EVALUATOR = "evaluator"
SPECIFIC_CONFIG_PATH = "config/specific_evaluator_config/"
START_PENDING_EVAL_NOTE = "0"  # force exception
INIT_EVAL_NOTE = 0
START_EVAL_PERTINENCE = 1
MAX_TA_EVAL_TIME_SECONDS = 0.1
DEFAULT_WEBSOCKET_REAL_TIME_EVALUATOR_REFRESH_RATE_SECONDS = 1
DEFAULT_REST_REAL_TIME_EVALUATOR_REFRESH_RATE_SECONDS = 60
CONFIG_REFRESH_RATE = "refresh_rate_seconds"
CONFIG_TIME_FRAME = "time_frame"
CONFIG_FILE_EXT = ".json"
CONFIG_CRYPTO_CURRENCIES = "crypto_currencies"
CONFIG_CRYPTO_PAIRS = "pairs"

# Socials
SOCIAL_EVALUATOR_NOT_THREADED_UPDATE_RATE = 1

# Stats
STATS_EVALUATOR_HISTORY_TIME = "relevant_history_months"
STATS_EVALUATOR_MAX_HISTORY_TIME = 3

# Tools
DIVERGENCE_USED_VALUE = 30

# Interfaces
CONFIG_INTERFACES = "interfaces"
CONFIG_INTERFACES_WEB = "web"
CONFIG_INTERFACES_TELEGRAM = "telegram"

# Packages
GITHUB = "github"
GITHUB_RAW_CONTENT_URL = "https://raw.githubusercontent.com"
GITHUB_BASE_URL = "https://github.com"
PACKAGES_PUBLIC_REPOSITORY = "Drakkar-Software/Octobot-Tentacles"
PACKAGES_PUBLIC_LIST = "packages_list.json"
PACKAGES_DEFAULT_BRANCH = "master"
EVALUATOR_DEFAULT_FOLDER = "Default"
EVALUATOR_ADVANCED_FOLDER = "Advanced"
CONFIG_PACKAGES_KEY = "packages"
PACKAGE_DESCRIPTION = "package_description"
PACKAGE_DESCRIPTION_LOCALISATION = "localisation"
PACKAGE_DESCRIPTION_IS_URL = "is_url"


class EvaluatorMatrixTypes(Enum):
    TA = "TA"
    SOCIAL = "SOCIAL"
    REAL_TIME = "REAL_TIME"
    STRATEGIES = "STRATEGIES"


class EvaluatorStates(Enum):
    SHORT = 1
    VERY_SHORT = 2
    LONG = 3
    VERY_LONG = 4
    NEUTRAL = 5


class EvaluatorsPertinence(Enum):
    SocialEvaluator = 0  # temp
    TAEvaluator = 1


class PriceStrings(Enum):
    STR_PRICE_TIME = "time"
    STR_PRICE_CLOSE = "close"
    STR_PRICE_OPEN = "open"
    STR_PRICE_HIGH = "high"
    STR_PRICE_LOW = "low"
    STR_PRICE_VOL = "vol"


class PriceIndexes(Enum):
    IND_PRICE_TIME = 0
    IND_PRICE_OPEN = 1
    IND_PRICE_HIGH = 2
    IND_PRICE_LOW = 3
    IND_PRICE_CLOSE = 4
    IND_PRICE_VOL = 5


class TimeFrames(Enum):
    ONE_MINUTE = "1m"
    THREE_MINUTES = "3m"
    FIVE_MINUTES = "5m"
    FIFTEEN_MINUTES = "15m"
    THIRTY_MINUTES = "30m"
    ONE_HOUR = "1h"
    TWO_HOURS = "2h"
    FOUR_HOURS = "4h"
    HEIGHT_HOURS = "8h"
    TWELVE_HOURS = "12h"
    ONE_DAY = "1d"
    THREE_DAYS = "3d"
    ONE_WEEK = "1w"
    ONE_MONTH = "1M"


TimeFramesMinutes = {
    TimeFrames.ONE_MINUTE: 1,
    TimeFrames.THREE_MINUTES: 3,
    TimeFrames.FIVE_MINUTES: 5,
    TimeFrames.FIFTEEN_MINUTES: 15,
    TimeFrames.THIRTY_MINUTES: 30,
    TimeFrames.ONE_HOUR: 60,
    TimeFrames.TWO_HOURS: 120,
    TimeFrames.FOUR_HOURS: 240,
    TimeFrames.HEIGHT_HOURS: 480,
    TimeFrames.TWELVE_HOURS: 720,
    TimeFrames.ONE_DAY: 1440,
    TimeFrames.THREE_DAYS: 4320,
    TimeFrames.ONE_WEEK: 10080,
    TimeFrames.ONE_MONTH: 43200,
}

# ladder : 1-100
TimeFramesRelevance = {
    TimeFrames.ONE_MINUTE: 5,
    TimeFrames.THREE_MINUTES: 5,
    TimeFrames.FIVE_MINUTES: 5,
    TimeFrames.FIFTEEN_MINUTES: 15,
    TimeFrames.THIRTY_MINUTES: 30,
    TimeFrames.ONE_HOUR: 50,
    TimeFrames.TWO_HOURS: 50,
    TimeFrames.FOUR_HOURS: 50,
    TimeFrames.HEIGHT_HOURS: 30,
    TimeFrames.TWELVE_HOURS: 30,
    TimeFrames.ONE_DAY: 30,
    TimeFrames.THREE_DAYS: 15,
    TimeFrames.ONE_WEEK: 15,
    TimeFrames.ONE_MONTH: 5,
}

IMAGE_ENDINGS = ["png", "jpg", "jpeg", "gif", "jfif", "tiff", "bmp", "ppm", "pgm", "pbm", "pnm", "webp", "hdr", "heif",
                 "bat", "bpg", "svg", "cgm"]


class TradeOrderSide(Enum):
    BUY = "buy"
    SELL = "sell"


class OrderStatus(Enum):
    FILLED = "closed"
    OPEN = "open"
    PARTIALLY_FILLED = "partially_filled"
    CANCELED = "canceled"
    CLOSED = "closed"


class TraderOrderType(Enum):
    BUY_MARKET = 1
    BUY_LIMIT = 2
    TAKE_PROFIT = 3
    TAKE_PROFIT_LIMIT = 4
    STOP_LOSS = 5
    STOP_LOSS_LIMIT = 6
    SELL_MARKET = 7
    SELL_LIMIT = 8


class ExchangeConstantsTickersColumns(Enum):
    SYMBOL = "symbol"
    TIMESTAMP = "timestamp"
    DATETIME = "datetime"
    HIGH = "high"
    LOW = "low"
    BID = "bid"
    BID_VOLUME = "bidVolume"
    ASK = "ask"
    ASK_VOLUME = "askVolume"
    VWAP = "vwap"
    OPEN = "open"
    CLOSE = "close"
    LAST = "last"
    PREVIOUS_CLOSE = "previousClose"
    CHANGE = "change"
    PERCENTAGE = "percentage"
    AVERAGE = "average"
    BASE_VOLUME = "baseVolume"
    QUOTE_VOLUME = "quoteVolume"
    INFO = "info"


class ExchangeConstantsTickersInfoColumns(Enum):
    SYMBOL = "symbol"
    PRICE_CHANGE = "priceChange"
    PRICE_CHANGE_PERCENT = "priceChangePercent"
    WEIGHTED_AVERAGE_PRICE = "weightedAvgPrice"
    PREVIOUS_CLOSE_PRICE = "prevClosePrice"
    LAST_PRICE = "lastPrice"
    LAST_QUANTITY = "lastQty"
    BID_PRICE = "bidPrice"
    BID_QUANTITY = "bidQty"
    ASK_PRICE = "askPrice"
    ASK_QUANTITY = "askQty"
    OPEN_PRICE = "openPrice"
    HIGH_PRICE = "highPrice"
    LOW_PRICE = "lowPrice"
    VOLUME = "volume"
    QUOTE_VOLUME = "quoteVolume"
    OPEN_TIME = "openTime"
    CLOSE_TIME = "closeTime"
    FIRST_ID = "firstId"
    LAST_ID = "lastId"
    COUNT = "count"


class ExchangeConstantsMarketStatusColumns(Enum):
    SYMBOL = "symbol"
    ID = "id"
    CURRENCY = "base"
    MARKET = "quote"
    ACTIVE = "active"
    PRECISION = "precision"  # number of decimal digits "after the dot"
    PRECISION_PRICE = "price"
    PRECISION_AMOUNT = "amount"
    PRECISION_COST = "cost"
    LIMITS = "limits"  # value limits when placing orders on this market
    LIMITS_AMOUNT = "amount"
    LIMITS_AMOUNT_MIN = "min"  # order amount should be > min
    LIMITS_AMOUNT_MAX = "max"  # order amount should be < max
    LIMITS_PRICE = "price"  # same min/max limits for the price of the order
    LIMITS_PRICE_MIN = "min"  # order price should be > min
    LIMITS_PRICE_MAX = "max"  # order price should be < max
    LIMITS_COST = "cost"  # same limits for order cost = price * amount
    LIMITS_COST_MIN = "min"  # order cost should be > min
    LIMITS_COST_MAX = "max"  # order cost should be < max
    INFO = "info"
