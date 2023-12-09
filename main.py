from Utils.ImportCsv import ImportParkingPriceList
if __name__ == '__main__':
    importer = ImportParkingPriceList()
    data = importer.import_parking_price_list("SampleData.csv")
    data.print()