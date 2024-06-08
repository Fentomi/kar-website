<template>
  <div class="wrapper">
    <v-expansion-panels class="mb-4" multiple>
      <v-expansion-panel
        v-for="data, index in items"
        :title="data"
        :key="index"
      > 
        <v-expansion-panel-text>
          <!-- Оборудование -->
          <div v-if="index === widgetEnum.equipment">
            <!-- Добавление оборудования -->
            <btn-with-form-dialog
              header-text="Добавление оборудования"
              btn-text="Добавить"
              @reset-btn-actions="resetBtnActions"
              :max-width="1200"
              :is-access-action="isAccessAction"
              :is-error-action="isErrorAction"
              :addFunction="equipmentAddFunction"
              is-add
            >
              <v-text-field
                v-for="data, index in equipmentDialogInputItems" :key="index"
                v-model="data.dataModel"
                :label="data.labelText"
              />
            </btn-with-form-dialog>
            <!-- Редактирование оборудования -->
            <btn-with-form-dialog
              header-text="Редактирование оборудования"
              btn-text="Редактировать"
              @reset-btn-actions="resetBtnActions"
              :max-width="1200"
              :is-access-action="isAccessAction"
              :is-error-action="isErrorAction"
              :editFunction="equpmentEditFunction"
              is-edit
            >
              <v-text-field
                v-for="data, index in equipmentDialogInputItems" :key="index"
                v-model="data.dataModel"
                :label="data.labelText"
              />
            </btn-with-form-dialog>
            <!-- Списание оборудования -->
            <btn-with-form-dialog
              header-text="Списание оборудования"
              btn-text="Списать"
              @reset-btn-actions="resetBtnActions"
              :max-width="1200"
              :is-access-action="isAccessAction"
              :is-error-action="isErrorAction"
              :deleteFunction="equipmentDeleteFunction"
              is-delete
            >
              <v-text-field
                v-for="data, index in equipmentDialogInputItems" :key="index"
                v-model="data.dataModel"
                :label="data.labelText"
              />
            </btn-with-form-dialog>
            <!-- Посмотреть записи оборудования -->
            <btn-with-list-dialog
              header-text="Список оборудования"
              btn-text="Посмотреть записи"
              :max-width="700"
              :headers="EquipmentListDialogHeaders"
              :items="equipmentListDialogItems"
            />
          </div>
          <!-- МОЛы -->
          <div v-if="index === widgetEnum.employees">
            <!-- Добавить МОЛа -->
            <btn-with-form-dialog
              header-text="Добавление МОЛа"
              btn-text="Добавить"
              @reset-btn-actions="resetBtnActions"
              :max-width="1200"
              :is-access-action="isAccessAction"
              :is-error-action="isErrorAction"
              :addFunction="employeeAddFunc"
              is-add
            >
              <v-text-field
                v-for="data, index in employeesDialogInputItems" :key="index"
                v-model="data.dataModel"
                :label="data.labelText"
              />
            </btn-with-form-dialog>
            <!-- Редактирование МОЛа -->
            <btn-with-form-dialog
              header-text="Редактирование МОЛа"
              btn-text="Редактировать"
              @reset-btn-actions="resetBtnActions"
              :max-width="1200"
              :is-access-action="isAccessAction"
              :is-error-action="isErrorAction"
              :editFunction="employeeEditFunc"
              is-edit
            >
              <v-text-field
                v-for="data, index in employeesDialogInputItems" :key="index"
                v-model="data.dataModel"
                :label="data.labelText"
              />
            </btn-with-form-dialog>
            <!-- Увольнение МОЛа -->
            <btn-with-form-dialog
              header-text="Отстранение МОЛа"
              btn-text="Отстранить"
              @reset-btn-actions="resetBtnActions"
              :max-width="1200"
              :is-access-action="isAccessAction"
              :is-error-action="isErrorAction"
              :deleteFunction="employeeDeleteFunc"
              is-delete
            >
              <v-text-field
                v-for="data, index in employeesDialogInputItems" :key="index"
                v-model="data.dataModel"
                :label="data.labelText"
              />
            </btn-with-form-dialog>
            <v-btn @click="" class="mr-1 mb-2"> Доверенное оборудование </v-btn>
            <!-- Посмотреть записи МОЛов -->
            <btn-with-list-dialog
              header-text="Список сотрудников"
              btn-text="Посмотреть записи"
              :max-width="450"
              :headers="EmployeesListDialogHeaders"
              :items="employeesListDialogItems"
            />
          </div>
          <!-- Помещения -->
          <div v-if="index === widgetEnum.premises">
            <!-- Посмотреть записи помещений -->
            <btn-with-list-dialog
              header-text="Список помещений"
              btn-text="Посмотреть записи"
              :max-width="650"
              :headers="PremisesListDialogHeader"
              :items="PremisesListDialogItems"
            />
          </div>
          <!-- Отчеты -->
          <div v-if="index === widgetEnum.reports">
            <btn-with-form-dialog
              header-text="Отчетов нет"
              btn-text="Посмотреть отчеты"
              :max-width="300"
            />
          </div>
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
    <v-btn style="width: 100%" @click="this.$emit('logout')">Выход из системы</v-btn>
  </div>
</template>

<script>
import BtnWithListDialog from '@/components/widgets/BtnWithListDialog.vue';
import BtnWithFormDialog from '@/components/widgets/BtnWithFormDialog.vue';
import axios from 'axios';

export default {
  components: { BtnWithListDialog, BtnWithFormDialog },
  data() {
    return {
      items: [ 'Оборудование', 'Сотрудники', 'Помещения', 'Отчеты' ],
      widgetEnum: { equipment: 0, employees: 1, premises: 2, reports: 3 },
      equipmentListDialogItems: [],
      employeesListDialogItems: [],
      equipmentDialogInputItems: [
        { dataModel: '', labelText: 'Код оборудования' },
        { dataModel: '', labelText: 'Инвентарный номер' },
        { dataModel: '', labelText: 'Состояние' },
        { dataModel: '', labelText: 'Код типа оборудования' },
      ],
      employeesDialogInputItems: [
        { dataModel: '', labelText: 'Код МОЛа' },
        { dataModel: '', labelText: 'Код сотрудника' },
        { dataModel: '', labelText: 'Начало ответственности' }
      ],
      isAccessAction: false,
      isErrorAction: false,
    }
  },
  methods: {
    resetBtnActions() {
      this.isAccessAction = false;
      this.isErrorAction = false;
    },
    async equipmentAddFunction() {
      if(!this.equipmentDialogInputItems.every(item => item.dataModel)) return this.isErrorAction = true;
      this.isAccessAction = true;
      await axios.post('http://127.0.0.1:5000/data/equipment', {
        kod_oborud: Number(this.equipmentDialogInputItems[0].dataModel),
        invent_nomer: Number(this.equipmentDialogInputItems[1].dataModel),
        sostoyanie: this.equipmentDialogInputItems[2].dataModel,
        kod_tipa_ucheta: Number(this.equipmentDialogInputItems[3].dataModel),
        method: 'ADD',
      }).finally(async () => {
        await this.getEquipmentListDialogItems();
      });
      this.equipmentDialogInputItems = this.equipmentDialogInputItems.map(item => { return { dataModel: '', labelText: item.labelText }});
    },
    async equpmentEditFunction() {
      if(!this.equipmentDialogInputItems.every(item => item.dataModel)) return this.isErrorAction = true;
      this.isAccessAction = true;
      await axios.post('http://127.0.0.1:5000/data/equipment', {
        kod_oborud: Number(this.equipmentDialogInputItems[0].dataModel),
        invent_nomer: Number(this.equipmentDialogInputItems[1].dataModel),
        sostoyanie: this.equipmentDialogInputItems[2].dataModel,
        kod_tipa_ucheta: Number(this.equipmentDialogInputItems[3].dataModel),
        method: 'EDIT',
      }).finally(async () => {
        await this.getEquipmentListDialogItems();
      });
      this.equipmentDialogInputItems = this.equipmentDialogInputItems.map(item => { return { dataModel: '', labelText: item.labelText }});
    },
    async equipmentDeleteFunction() {
      if(!this.equipmentDialogInputItems.every(item => item.dataModel)) return this.isErrorAction = true;
      this.isAccessAction = true;
      await axios.post('http://127.0.0.1:5000/data/equipment', {
        kod_oborud: Number(this.equipmentDialogInputItems[0].dataModel),
        invent_nomer: Number(this.equipmentDialogInputItems[1].dataModel),
        sostoyanie: this.equipmentDialogInputItems[2].dataModel,
        kod_tipa_ucheta: Number(this.equipmentDialogInputItems[3].dataModel),
        method: 'DELETE',
      }).finally(async () => {
        await this.getEquipmentListDialogItems();
      });
      this.equipmentDialogInputItems = this.equipmentDialogInputItems.map(item => { return { dataModel: '', labelText: item.labelText }});
    },
    async employeeAddFunc() {
      if(!this.employeesDialogInputItems.every(item => item.dataModel)) return this.isErrorAction = true;
      this.isAccessAction = true;
      await axios.post('http://127.0.0.1:5000/data/mol', {
        kod_MOL: Number(this.employeesDialogInputItems[0].dataModel),
        kod_sotr: Number(this.employeesDialogInputItems[1].dataModel),
        nach_otvetst: this.employeesDialogInputItems[2].dataModel,
        method: 'ADD',
      }).finally(async () => {
        await this.getEmplyeesListDialogItems();
      });
      this.employeesDialogInputItems = this.employeesDialogInputItems.map(item => { return { dataModel: '', labelText: item.labelText }});
    },
    async employeeEditFunc() {
      if(!this.employeesDialogInputItems.every(item => item.dataModel)) return this.isErrorAction = true;
      this.isAccessAction = true;
      await axios.post('http://127.0.0.1:5000/data/mol', {
        kod_MOL: Number(this.employeesDialogInputItems[0].dataModel),
        kod_sotr: Number(this.employeesDialogInputItems[1].dataModel),
        nach_otvetst: this.employeesDialogInputItems[2].dataModel,
        method: 'EDIT',
      }).finally(async () => {
        await this.getEmplyeesListDialogItems();
      });
      this.employeesDialogInputItems = this.employeesDialogInputItems.map(item => { return { dataModel: '', labelText: item.labelText }});
    },
    async employeeDeleteFunc() {
      if(!this.employeesDialogInputItems.every(item => item.dataModel)) return this.isErrorAction = true;
      this.isAccessAction = true;
      await axios.post('http://127.0.0.1:5000/data/mol', {
        kod_MOL: Number(this.employeesDialogInputItems[0].dataModel),
        kod_sotr: Number(this.employeesDialogInputItems[1].dataModel),
        nach_otvetst: this.employeesDialogInputItems[2].dataModel,
        method: 'DELETE',
      }).finally(async () => {
        await this.getEmplyeesListDialogItems();
      });
      this.employeesDialogInputItems = this.employeesDialogInputItems.map(item => { return { dataModel: '', labelText: item.labelText }});
    },
    async getEquipmentListDialogItems() {
      await axios.get('http://127.0.0.1:5000/data/equipment').then(response => {
        this.equipmentListDialogItems = response.data;
      }).catch(err => console.error(err));
    },
    async getEmplyeesListDialogItems() {
      await axios.get('http://127.0.0.1:5000/data/mol').then(response => {
        this.employeesListDialogItems = response.data;
      }).catch(err => console.error(err));
    }
  },
  computed: {
    EquipmentListDialogHeaders() {
      return [
        { title: 'Код оборудования', align: 'start', key: 'kod_oborud' },
        { title: 'Инвентарный номер', align: 'end', key: 'invent_nomer' },
        { title: 'Состояние', align: 'end', key: 'sostoyanie' },
        { title: 'Код типа оборудования', align: 'end', key: 'kod_tipa_ucheta' },
      ]; 
    },
    EmployeesListDialogHeaders() {
      return [
        { title: 'Код МОЛа', align: 'start', key: 'kod_MOL'},
        { title: 'Код сотрудника', align: 'start', key: 'kod_sotr'},
        { title: 'Начало ответственности', align: 'center', key: 'nach_otvetst'},
      ];
    },
    PremisesListDialogHeader() {
      return [
        { title: 'id', align: 'start', key: 'id'},
        { title: 'Код помещения', align: 'start', key: 'roomСode'},
        { title: 'Название помещения', align: 'center', key: 'roomName'},
        { title: 'Номер помещения', align: 'center', key: 'roomNumber'},
        { title: 'Код подразделения', align: 'center', key: 'departmentCode'},
      ];
    },
    PremisesListDialogItems() {
      return [
        { id: 1, roomСode: 100, roomName: 'Столовая', roomNumber: 100500, departmentCode: 320},
        { id: 2, roomСode: 101, roomName: 'Гостинная', roomNumber: 100501, departmentCode: 320},
        { id: 3, roomСode: 102, roomName: 'Диванная', roomNumber: 100502, departmentCode: 320},
        { id: 4, roomСode: 103, roomName: 'Стуловая', roomNumber: 100503, departmentCode: 420},
        { id: 5, roomСode: 104, roomName: 'Коверная', roomNumber: 100504, departmentCode: 420},
      ]
    },
  },
  async created() {
    await this.getEquipmentListDialogItems();
    await this.getEmplyeesListDialogItems();
  },
}
</script>