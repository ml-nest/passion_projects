
## File Desc
# sales_train.csv - the training set. Daily historical data from January 2013 to October 2015.
# test.csv - the test set. You need to forecast the sales for these shops and products for November 2015.
# sample_submission.csv - a sample submission file in the correct format.
# items.csv - supplemental information about the items/products.
# item_categories.csv  - supplemental information about the items categories.
# shops.csv- supplemental information about the shops.

## Data dictionary
# ID - an Id that represents a (Shop, Item) tuple within the test set
# shop_id - unique identifier of a shop
# item_id - unique identifier of a product
# item_category_id - unique identifier of item category
# item_cnt_day - number of products sold. You are predicting a monthly amount of this measure
# item_price - current price of an item
# date - date in format dd/mm/yyyy
# date_block_num - a consecutive month number, used for convenience. January 2013 is 0, February 2013 is 1,..., October 2015 is 33
# item_name - name of item
# shop_name - name of shop
# item_category_name - name of item category


### Importing packages

# Basic
import pandas as pd

# Data preprocessing
from sklearn.preprocessing import LabelEncoder


## Reading the dataset

cats = pd.read_csv('data/item_categories.csv')
items = pd.read_csv('data/items.csv')
train = pd.read_csv('data/sales_train.csv')
test = pd.read_csv('data/test.csv')
shops = pd.read_csv('data/shops.csv')


### Data preprocessing

## items_cat
items_cat['split'] = items_cat['item_category_name'].str.split('-')
items_cat['type'] = items_cat['split'].map(lambda x: x[0].strip())
items_cat['type_code'] = LabelEncoder().fit_transform(items_cat['type'])
# if subtype is nan then type
items_cat['subtype'] = items_cat['split'].map(lambda x: x[1].strip() if len(x) > 1 else x[0].strip())
items_cat['subtype_code'] = LabelEncoder().fit_transform(items_cat['subtype'])
items_cat = items_cat[['item_category_id','type_code', 'subtype_code']]


## items
items.head()        
# # Create the date the product was first sold as a feature
# items['first_sale_month'] = train.groupby('item_id').agg({'date_block_num': 'min'})['date_block_num']
# # Refine null values in items table
# items = items.apply(lambda x: x.fillna(x.median()) if x.dtype != "O" else x, axis=0)


## Shop details

shop_detail.head()

# Cleaning out shop names
shop_detail['shop_name'] = shop_detail['shop_name'].str.replace('"', '')
shop_detail['shop_name'] = shop_detail['shop_name'].str.replace('!', '')

# Extracting out city names from the shop names
shop_detail['city'] = shop_detail['shop_name'].apply(lambda x: x.split()[0])
# Encoding and removing the names
shop_detail['city'] = LabelEncoder().fit_transform(shop_detail['city'])


## Training dataset

# Change data type for date calculation
train["date"] = pd.to_datetime(train["date"], format="%d.%m.%Y")

# # Merge some duplicate shops
# train["shop_id"] = train["shop_id"].replace({0: 57, 1: 58, 11: 10, 40: 39})
# # Keep only shops that are in the test set
# train = train.loc[train.shop_id.isin(test["shop_id"].unique()), :]

# Drop training items with extreme or negative prices or sales counts
train = train[(train["item_price"] > 0) & (train["item_price"] < 25000)]
train = train[(train["item_cnt_day"] > 0) & (train["item_cnt_day"] < 1000)]


# Merge data
train = train.merge(shop_detail, on='shop_id', how='left')
train = train.merge(items, on='item_id', how='left')
train = train.merge(items_cat, on='item_category_id', how='left')
test = test.merge(shops, on='shop_id', how='left')
test = test.merge(items, on='item_id', how='left')
test = test.merge(cats, on='item_category_id', how='left')