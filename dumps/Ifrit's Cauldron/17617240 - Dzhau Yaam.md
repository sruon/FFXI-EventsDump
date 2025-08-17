# 17617240 - Dzhau Yaam

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Ifrit's Cauldron (ID: 205) |
| Block Size       | 164 bytes                  |
| Total Events     | 6                          |
| References Count | 8                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [28](#event-28)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |     24 |              5 |
| [65535.3](#event-655353) | 0x0024       |     27 |              3 |
| [65535.4](#event-655354) | 0x003F       |     27 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFC518A  |  4294726026 |
|       1 | 0x511C0     |      332224 |
|       2 | 0xFFFFCEDA  |  4294954714 |
|       3 | 0x0A61      |        2657 |
|       4 | 0x0000      |           0 |
|       5 | 0x0001      |           1 |
|       6 | 0x0080      |         128 |
|       7 | 0x0026      |          38 |

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

### Event 28

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-241.270*, z=332.224*, y=-12.582*, direction=233.5°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 24 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      22 00 2F 00              "./.
0010: F8 FF FF 7F 92 01 F8 FF  FF 7F 6C F8 FF FF 7F 04  ..........l.....
0020: 80 05 80 00                                       ....            
```

#### Opcodes

```
  0: 0x000C [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x000E [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0014 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x001A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  4: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             6C F8 FF FF  7F 06 80 05 80 9F 07 80      l...........
0030: F8 FF FF 7F F8 FF FF 7F  6D 61 69 6E 04 80 00     ........main... 
```

#### Opcodes

```
  0: 0x0024 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x002D [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[38*, 0*]
  2: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               6C                 l
0040: F8 FF FF 7F 04 80 05 80  9F 07 80 F8 FF FF 7F F8  ................
0050: FF FF 7F 73 74 6F 70 04  80 00                    ...stop...      
```

#### Opcodes

```
  0: 0x003F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0048 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "stop" with entities [EventEntity, EventEntity], work=[38*, 0*]
  2: 0x0059 [0x00] END_REQSTACK()
```
