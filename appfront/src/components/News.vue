<template>
  <div class="border">
    <div style="margin: 30px;">
      <el-form ref="form" :model="form" label="80px">
        <el-form-item label="您的姓名">
          <el-input v-model="form.author" placeholder="新闻稿编辑者姓名，如：魏家伟"></el-input>
        </el-form-item>

        <el-form-item label="活动类型">
          <el-select v-model="form.type" placeholder="请选择活动类型">
            <el-option label="讲座" value="讲座"></el-option>
            <el-option label="项目讨论" value="项目讨论"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="活动主题">
          <el-input v-model="form.topic" placeholder="如：Zerotier"></el-input>
        </el-form-item>

        <el-form-item label="活动日期">
          <el-input v-model="form.time" placeholder="格式为 X月X日，如：4月11日"></el-input>
        </el-form-item>

        <el-form-item label="活动地点">
          <el-input v-model="form.position" placeholder="如：一教B307"></el-input>
        </el-form-item>

        <el-form-item label="活动主持人员">
          <el-input v-model="form.members" placeholder="指开讲座的人，如：腐竹"></el-input>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="onSubmit">生成新闻</el-button>
          <el-button @click="showExample">自动填写示例</el-button>
        </el-form-item>
      </el-form>
    </div>
    <el-divider></el-divider>
    <div style="margin: 30px">
      {{ content }}
    </div>
    <el-divider></el-divider>
  </div>

</template>

<script>

export default {
  name: 'News',
  data () {
    return {
      form: {
        author: '',
        type: '',
        topic: '',
        time: '',
        position: '',
        members: ''
      },
      content: ''
    }
  },
  mounted () {
    this.content = '这是一段示例文档'
  },
  methods: {
    onSubmit () {
      this.$axios({
        method: 'post',
        url: '../api/generate',
        data: this.form
      })
        .then(
          successResponse => {
            console.log('success')
            console.log(successResponse.data)
            console.log(successResponse.data['method'])
            console.log(successResponse.data['content'])
            this.content = successResponse.data['content']
          }
        )
        .catch(failResponse => {
          console.log('fail')
        })
    },
    showExample () {
      this.form.author = '魏家伟'
      this.form.type = '讲座'
      this.form.topic = 'Zerotier'
      this.form.time = '4月11日'
      this.form.position = '一教B307'
      this.form.members = '李航帆'
    }
  }
}
</script>

<style scoped>
.border{
  border-radius: 30px;
  width: 60%;
  background-color: rgba(255, 255, 255, 1);
  box-shadow: 5px 5px 5px 5px gray;
  margin: 5% 20% 5% 20%;
}
</style>
