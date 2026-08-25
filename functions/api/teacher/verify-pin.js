// Cloudflare Pages Serverless Function for /api/teacher/verify-pin
export async function onRequestPost(context) {
  try {
    const body = await context.request.json();
    const inputPin = (body.pin || '').trim();

    // Cloudflare Pages 환경변수 TEACHER_PIN 읽기 (기본값: 1234,admin)
    const envPinStr = context.env.TEACHER_PIN || '1234,admin';
    const configuredPins = envPinStr
      .split(',')
      .map(p => p.trim())
      .filter(Boolean);

    if (configuredPins.includes(inputPin)) {
      return new Response(JSON.stringify({ success: true, message: '교사 인증 성공' }), {
        headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' }
      });
    } else {
      return new Response(JSON.stringify({ success: false, message: '선생님 비밀번호가 일치하지 않습니다.' }), {
        status: 401,
        headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' }
      });
    }
  } catch (err) {
    return new Response(JSON.stringify({ success: false, message: '요청 처리 실패: ' + err.message }), {
      status: 400,
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' }
    });
  }
}
