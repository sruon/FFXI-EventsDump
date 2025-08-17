# 17633352 - Talking Doll

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Cloister of Tremors (ID: 209) |
| Block Size       | 232 bytes                     |
| Total Events     | 8                             |
| References Count | 18                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |     12 |              3 |
| [65535.4](#event-655354) | 0x0033       |     23 |              5 |
| [65535.5](#event-655355) | 0x004A       |     10 |              2 |
| [65535.6](#event-655356) | 0x0054       |     10 |              2 |
| [32000](#event-32000)    | 0x005E       |     18 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00FC      |         252 |
|       1 | 0x001E      |          30 |
|       2 | 0x0032      |          50 |
|       3 | 0x0001      |           1 |
|       4 | 0x57F4      |       22516 |
|       5 | 0x7B08      |       31496 |
|       6 | 0xFFFFBB4F  |  4294949711 |
|       7 | 0x0E0E      |        3598 |
|       8 | 0x0064      |         100 |
|       9 | 0x0078      |         120 |
|      10 | 0x59C7      |       22983 |
|      11 | 0x7A25      |       31269 |
|      12 | 0xFFFFB8E7  |  4294949095 |
|      13 | 0x05DD      |        1501 |
|      14 | 0x66E6      |       26342 |
|      15 | 0x7B67      |       31591 |
|      16 | 0xFFFFB5AD  |  4294948269 |
|      17 | 0x0400      |        1024 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 62 72 75 30   [..........bru0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bru0" with entities [EventEntity, EventEntity], work=252*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 62 72 75 30 5E 69   S........bru0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bru0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      6C  F8 FF FF 7F 02 80 03 80         l........
0030: 33 00 00                                          3..             
```

#### Opcodes

```
  0: 0x0027 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=50*, fade_time=1*)
  1: 0x0030 [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  2: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          22 00 33 01 37  04 80 05 80 06 80 07 80     ".3.7........
0040: 6C F8 FF FF 7F 08 80 09  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0033 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0035 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x0037 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=22.516*, z=31.496*, y=-17.585*, direction=316.2°*
  3: 0x0040 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=100*, fade_time=120*)
  4: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                37 0A 80 0B 80 0C            7.....
0050: 80 0D 80 00                                       ....            
```

#### Opcodes

```
  0: 0x004A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=22.983*, z=31.269*, y=-18.201*, direction=131.9°*
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             37 0E 80 0F  80 10 80 11 80 00            7.........  
```

#### Opcodes

```
  0: 0x0054 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=26.342*, z=31.591*, y=-19.027*, direction=90.0°*
  1: 0x005D [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            6C F8                l.
0060: FF FF 7F 02 80 03 80 33  00 92 01 F8 FF FF 7F 00  .......3........
```

#### Opcodes

```
  0: 0x005E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=50*, fade_time=1*)
  1: 0x0067 [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  2: 0x0069 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x006F [0x00] END_REQSTACK()
```
