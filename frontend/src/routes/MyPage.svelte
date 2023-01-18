<script>
  import fastapi from "../lib/api";
  import { link } from "svelte-spa-router";
  import { is_login } from "../lib/store";
  import Navigation from "../components/Navigation.svelte";
  import moment from "moment/min/moment-with-locales";
  moment.locale("ko");

  let birthday_list = [];

  function get_birthday_list() {
    let params = {};
    fastapi("get", "/api/birthday/list", params, (json) => {
      birthday_list = json.birthday_list;
    });
  }

  $: get_birthday_list();
</script>

<Navigation />

<div class="container my-3">
  <table class="table">
    <thead>
      <tr class="text-center table-dark">
        <th>번호</th>
        <th>이름</th>
        <th>생일</th>
        <th>생성일시</th>
      </tr>
    </thead>

    <tbody>
      {#each birthday_list as birthday, i}
        <tr class="text-center">
          <td>{i}</td>
          <td class="text-center">
            <a use:link href="/birthday-detail/{birthday.id}">{birthday.name}</a
            >
            {#if birthday.messages.length > 0}
              <span class="text-danger small mx-2"
                >{birthday.messages.length}</span
              >
            {/if}
          </td>
          <td>{moment(birthday.bdate).format("MM/DD")}</td>
          <td>{moment(birthday.created_at).format("YYYY/MM/DD HH:mm")}</td>
        </tr>
      {/each}
    </tbody>
  </table>

  <a class="btn btn-primary" use:link href="/create-birthday" role="button"
    >추가하기</a
  >
</div>
