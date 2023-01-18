<script>
  import { push } from "svelte-spa-router";
  import fastapi from "../lib/api";
  import Error from "../components/Error.svelte";
  import Navigation from "../components/Navigation.svelte";

  let error = { detail: [] };
  let name = "";
  let bdate = "";
  let introduce = "";

  function post_question(event) {
    event.preventDefault();
    let url = "/api/birthday/create";
    let params = {
      name: name,
      bdate: bdate,
      introduce: introduce,
    };
    fastapi(
      "post",
      url,
      params,
      (json) => {
        push("/my-page");
      },
      (json_error) => {
        error = json_error;
      }
    );
  }
</script>

<Navigation />

<div class="container">
  <h5 class="my-3 border-bottom pb-2">생일 등록</h5>
  <Error {error} />
  <form method="post" class="my-3">
    <div class="mb-3">
      <label for="name">이름</label>
      <input type="text" class="form-control" bind:value={name} />
    </div>
    <div class="mb-3">
      <label for="bdate">날짜</label>
      <input type="date" class="form-control" bind:value={bdate} />
    </div>
    <div class="mb-3">
      <label for="introduce">소개 메시지</label>
      <textarea class="form-control" rows="10" bind:value={introduce} />
    </div>
    <button class="btn btn-primary" on:click={post_question}>저장하기</button>
  </form>
</div>
