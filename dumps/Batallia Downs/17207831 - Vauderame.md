# 17207831 - Vauderame

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Batallia Downs (ID: 105) |
| Block Size       | 156 bytes                |
| Total Events     | 4                        |
| References Count | 13                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [904](#event-904)        | 0x0001       |     20 |              3 |
| [65535.1](#event-655351) | 0x0015       |     18 |              6 |
| [65535.2](#event-655352) | 0x0027       |     30 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x320BF     |      204991 |
|       1 | 0xFFF6D262  |  4294365794 |
|       2 | 0x3CA4      |       15524 |
|       3 | 0x0288      |         648 |
|       4 | 0x000F      |          15 |
|       5 | 0x000D      |          13 |
|       6 | 0x327CC     |      206796 |
|       7 | 0xFFF6C4E5  |  4294362341 |
|       8 | 0x3B8A      |       15242 |
|       9 | 0x007A      |         122 |
|      10 | 0x002D      |          45 |
|      11 | 0x0000      |           0 |
|      12 | 0x0096      |         150 |

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

### Event 904

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 79 00 F8 FF FF 7F   7........y.....
0010: F0 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=204.991*, z=-601.502*, y=15.524*, direction=57.0°*
  1: 0x000A [0x79] EventEntity looks at LocalPlayer (Basic look)
  2: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                1C 04 80  32 05 80 1F 00 06 80 07       ...2.......
0020: 80 08 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0015 [0x1C] WAIT(15* ticks)
  1: 0x0018 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=206.796*, Z=-604.955*, Y=15.242*
  3: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0025 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 30 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      73  09 80 F8 FF FF 7F F8 FF         s........
0030: FF 7F 1C 0A 80 6C F8 FF  FF 7F 0B 80 0C 80 92 01  .....l..........
0040: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0027 [0x73] EventEntity casts magic 122* on EventEntity
  1: 0x0032 [0x1C] WAIT(45* ticks)
  2: 0x0035 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=150*)
  3: 0x003E [0x92] EventEntity->Render.Flags3 ^= 0x01
  4: 0x0044 [0x00] END_REQSTACK()
```
