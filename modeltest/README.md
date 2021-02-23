# model test project

브랜치, 커밋 레벨이 아닌 코드 레벨에서 모델 정의를 분리할 수 있을까에 대한 고민 프로젝트

> 실제 프로젝트에선 각 환경별 디비 스킴이 동일하도록 구성되는게 베스트 프랙티스라 생각한다.
> 하지만 세상의 모든일이 그렇듯 베스트 프랙티스를 따라가지 못하는 상황은 생겨나기 마련이고,
> 이를 대비하는 안티 패턴을 알아두고 필요 시 사용하는 자세도 필요하다 생각된다. (개인적인 의견)

## 얻고자 하는것

- 코드 레벨의 환경 별 모델 정의 분리

## environments

- python 3.9.1
- django 3.1
- django rest framework 3.12

## DJANGO_SETTINGS_MODULE export

production 레벨의 db 마이그레이션이 필요할 땐

```shell
export DJANGO_SETTINGS_MODULE=modeltest.settings.production

or

export DJANGO_SETTINGS_MODULE=modeltest.settings.
```