# 17772703 - Francmage

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 172 bytes                 |
| Total Events     | 5                         |
| References Count | 17                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10008](#event-10008)    | 0x0001       |     18 |              4 |
| [65535.1](#event-655351) | 0x0013       |     10 |              2 |
| [65535.2](#event-655352) | 0x001D       |     24 |              6 |
| [65535.3](#event-655353) | 0x0035       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0xFFFDD89B  |  4294826139 |
|       3 | 0x12B52     |       76626 |
|       4 | 0xFFFF932B  |  4294939435 |
|       5 | 0x0C73      |        3187 |
|       6 | 0x0028      |          40 |
|       7 | 0x52DC2     |      339394 |
|       8 | 0xFFFA9F8A  |  4294614922 |
|       9 | 0xFFFFFA24  |  4294965796 |
|      10 | 0x53CBB     |      343227 |
|      11 | 0xFFFAD8DE  |  4294629598 |
|      12 | 0xFFFFFF5D  |  4294967133 |
|      13 | 0x0008      |           8 |
|      14 | 0xFFFDD980  |  4294826368 |
|      15 | 0x14540     |       83264 |
|      16 | 0xFFFF930F  |  4294939407 |

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

### Event 10008

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 2F 00 F8 FF FF  7F 6C F8 FF FF 7F 00 80   "./.....l......
0010: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0009 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          37 02 80 03 80  04 80 05 80 00              7.........   
```

#### Opcodes

```
  0: 0x0013 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-141.157*, z=76.626*, y=-27.861*, direction=280.1°*
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         32 06 80               2..
0020: 1F 00 07 80 08 80 09 80  1F 01 1F 00 0A 80 0B 80  ................
0030: 0C 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x001D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0020 [0x1F] MOVE_ENTITY: EventEntity moves to X=339.394*, Z=-352.374*, Y=-1.500*
  2: 0x0028 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=343.227*, Z=-337.698*, Y=-0.163*
  4: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                32 0D 80  1F 00 0E 80 0F 80 10 80       2..........
0040: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0035 [0x32] ExtData[1]->MainSpeed = 8* * 0.1
  1: 0x0038 [0x1F] MOVE_ENTITY: EventEntity moves to X=-140.928*, Z=83.264*, Y=-27.889*
  2: 0x0040 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0042 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0043 [0x00] END_REQSTACK()
```
