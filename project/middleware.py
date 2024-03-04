from django.shortcuts import redirect


def pre_handle_request(get_response):
    def middleware(request):
        uri = request.get_full_path()

        # 미들웨어에 작성한 코드가 반영되면 안되는 uri가 있고,
        # 이 uri가 아니고,
        if 'admin' not in uri and 'accounts' not in uri and 'oauth' not in uri and 'api' not in uri:
            # 요청한 서비스가 로그인을 필요로 한다면,
            if 'join' not in uri and 'login' not in uri:
                # 세션에 member가 담겨있는지 검사한다. (로그인 여부)
                if request.session.get('member') is None:
                    # 로그인 전에 클릭한 페이지의 경로를 세션에 담아놓는다.
                    # 로그인 완료시에 바로 해당 경로로 이동할 수 있게 하기 위함.
                    request.session['previous_uri'] = uri
                    # 로그인 페이지로 이동
                    return redirect('/member/login')

            if request.user_agent.is_mobile:
                uri = f'/mobile/{uri}'
                request.path_info = uri

            # 모바일이 아니고
            else:
                uri.replace('/mobile', '')

        # 응답 전 처리
        response = get_response(request)
        # 응답 후 처리

        return response

    return middleware