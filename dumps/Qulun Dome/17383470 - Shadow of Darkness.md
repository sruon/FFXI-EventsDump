# 17383470 - Shadow of Darkness

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Qulun Dome (ID: 148) |
| Block Size       | 88 bytes             |
| Total Events     | 3                    |
| References Count | 6                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [0](#event-0)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     34 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x35DD      |       13789 |
|       1 | 0xFFFEA463  |  4294878307 |
|       2 | 0x62C5      |       25285 |
|       3 | 0x0B46      |        2886 |
|       4 | 0x0048      |          72 |
|       5 | 0x0001      |           1 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 34 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 37 00 80 01  80 02 80 03 80 6C F8 FF    ".7........l..
0010: FF 7F 04 80 05 80 2C 2E  40 09 01 2E 40 09 01 69  ......,.@...@..i
0020: 6E 69 74 00                                       nit.            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=13.789*, z=-88.989*, y=25.285*, direction=253.6°*
  2: 0x000D [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=72*, fade_time=1*)
  3: 0x0016 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "init" with entities [Shadow of Darkness (ID: 17383470/0x0109402E), Shadow of Darkness (ID: 17383470/0x0109402E)]
  4: 0x0023 [0x00] END_REQSTACK()
```
