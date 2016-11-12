from django.contrib import admin
from arboles.models import Arbol, Censista
from django.contrib.admin.views.decorators import staff_member_required
from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
import StringIO
import xlsxwriter

# Register your models here.

class ArbolAdmin(admin.ModelAdmin):
    list_display = ('especie', 'pub_date')

    def get_urls(self):
        urls = super(ArbolAdmin, self).get_urls()
        my_urls = patterns("",
            url(r"^exportExcel/$", exportExcel),
            url(r"^exportCsv/$", exportCSV)
        )
        return my_urls + urls


@staff_member_required
def exportExcel(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Arboles.xlsx'
    xls = writeToExcel(request)
    response.write(xls)
    return response

@staff_member_required
def exportCSV(request):

    return HttpResponseRedirect(request.META["HTTP_REFERER"])

def writeToExcel(request):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    censistas = Censista.objects.all()
    i = 1
    for c in (censistas):
        worksheet = createWorksheet(workbook, i)
        worksheet.write('A4', c.nombre)
        worksheet.write('B4', c.apellido)
        arboles = c.arbol_set.all()
        row = 10
        col = 0
        for arbol in (arboles):
            worksheet.write(row, col, arbol.calle)
            worksheet.write(row, col + 1, arbol.vereda)
            worksheet.write(row, col + 2, arbol.anchoVereda)
            worksheet.write(row, col + 3, arbol.nroFrente)
            worksheet.write(row, col + 4, arbol.nroArbol)
            worksheet.write(row, col + 5, arbol.especie)
            worksheet.write(row, col + 6, arbol.estadoSanitario)
            worksheet.write(row, col + 7, arbol.inclinacion)
            worksheet.write(row, col + 8, arbol.altInterCables)
            worksheet.write(row, col + 9, arbol.altInterLuminarias)
            worksheet.write(row, col + 10, arbol.altInterLuminarias)
            worksheet.write(row, col + 11, arbol.cazuela)
            worksheet.write(row, col + 11, arbol.distanciaEntrePlantas)
            worksheet.write(row, col + 12, arbol.distanciaAlMuro)
            worksheet.write(row, col + 13, arbol.podasAnteriores)
            worksheet.write(row, col + 14, arbol.circunferencia)
            worksheet.write(row, col + 15, arbol.observaciones)
            worksheet.write(row, col + 16, arbol.tipoDeTransito)
            http = "http://"
            imagenen1 = http + request.META['HTTP_HOST'] + arbol.imagen1.url if hasattr(arbol.imagen1, 'url') else "NO"
            imagenen2 = http + request.META['HTTP_HOST'] + arbol.imagen2.url if hasattr(arbol.imagen2, 'url') else "NO"
            imagenen3 = http + request.META['HTTP_HOST'] + arbol.imagen3.url if hasattr(arbol.imagen3, 'url') else "NO"
            imagenen4 = http + request.META['HTTP_HOST'] + arbol.imagen4.url if hasattr(arbol.imagen4, 'url') else "NO"
            imagenen5 = http + request.META['HTTP_HOST'] + arbol.imagen5.url if hasattr(arbol.imagen5, 'url') else "NO"
            imagenen6 = http + request.META['HTTP_HOST'] + arbol.imagen6.url if hasattr(arbol.imagen6, 'url') else "NO"
            imagenen7 = http + request.META['HTTP_HOST'] + arbol.imagen7.url if hasattr(arbol.imagen7, 'url') else "NO"
            imagenen8 = http + request.META['HTTP_HOST'] + arbol.imagen8.url if hasattr(arbol.imagen8, 'url') else "NO"
            imagenen9 = http + request.META['HTTP_HOST'] + arbol.imagen9.url if hasattr(arbol.imagen9, 'url') else "NO"
            imagenen10 = http + request.META['HTTP_HOST'] +  arbol.imagen10.url if hasattr(arbol.imagen10, 'url') else "NO"

            worksheet.write(row, col + 17, imagenen1)
            worksheet.write(row, col + 18, imagenen2)
            worksheet.write(row, col + 19, imagenen3)
            worksheet.write(row, col + 20, imagenen4)
            worksheet.write(row, col + 21, imagenen5)
            worksheet.write(row, col + 22, imagenen6)
            worksheet.write(row, col + 23, imagenen7)
            worksheet.write(row, col + 24, imagenen8)
            worksheet.write(row, col + 25, imagenen9)
            worksheet.write(row, col + 26, imagenen10)
            row += 1
        i+=1
    workbook.close()
    xlsx_data = output.getvalue()
    # xlsx_data contains the Excel file
    return xlsx_data

def createWorksheet(workbook, i):
    worksheet = workbook.add_worksheet("Censista " + str(i))
    title = workbook.add_format({
    'bold': True,
    'font_size': 14,
    'align': 'center',
    'valign': 'vcenter'
    })
    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1,
    })
    worksheet.set_column(0, 25, 25)

    worksheet.merge_range('A2:B2', 'Censista', header)
    worksheet.write('A3', 'Nombre', header)
    worksheet.write('B3', 'Apellido', header)

    # Here we will adding the code to add data
    worksheet.write('A10', 'Calle', header)
    worksheet.write('B10', 'Vereda', header)
    worksheet.write('C10', 'Ancho de Vereda', header)
    worksheet.write('D10', 'Nro. Frente', header)
    worksheet.write('E10', 'Nro. Arbol', header)
    worksheet.write('F10', 'Especie', header)
    worksheet.write('G10', 'Estado Sanitario', header)
    #worksheet.write('D2', 'S', header)
    #worksheet.write('E2', 'E', header)
    #worksheet.write('F2', 'D', header)
    worksheet.write('H10', 'Inclinacion', header)
    #worksheet.write('G2', 'NO', header)
    #worksheet.write('H2', 'LI', header)
    #worksheet.write('I2', 'MI', header)
    worksheet.write('I10', 'Altura Int Cables', header)
    #worksheet.write('J2', 'PD', header)
    #worksheet.write('K2', 'PE', header)
    #worksheet.write('L2', 'IA', header)
    worksheet.write('J10', 'Altura Int Luminarias', header)
    #worksheet.write('M2', 'PD', header)
    #worksheet.write('N2', 'PE', header)
    #worksheet.write('O2', 'IA', header)
    worksheet.write('K10', 'Cazuela', header)
    worksheet.write('L10', 'Distancia entre Plantas', header)
    worksheet.write('M10', 'Distancia al Muro', header)
    worksheet.write('N10', 'Podas Anteriores', header)
    worksheet.write('O10', 'Circunferencia', header)
    worksheet.write('P10', 'Observaciones', header)
    worksheet.write('Q10', 'Tipo de Transito', header)
    worksheet.write('R10', 'Imagen1', header)
    worksheet.write('S10', 'Imagen2', header)
    worksheet.write('T10', 'Imagen3', header)
    worksheet.write('U10', 'Imagen4', header)
    worksheet.write('V10', 'Imagen5', header)
    worksheet.write('W10', 'Imagen6', header)
    worksheet.write('X10', 'Imagen7', header)
    worksheet.write('Y10', 'Imagen8', header)
    worksheet.write('Z10', 'Imagen9', header)
    worksheet.write('AA10', 'Imagen10', header)
    return worksheet

admin.site.register(Arbol, ArbolAdmin)
admin.site.register(Censista)
