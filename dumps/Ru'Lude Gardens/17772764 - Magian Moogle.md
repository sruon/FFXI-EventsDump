# 17772764 - Magian Moogle

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 360 bytes                 |
| Total Events     | 11                        |
| References Count | 12                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10135](#event-10135)    | 0x0001       |      1 |              1 |
| [10136](#event-10136)    | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     29 |              8 |
| [65535.2](#event-655352) | 0x0020       |     46 |              7 |
| [65535.3](#event-655353) | 0x004E       |     20 |              7 |
| [65535.4](#event-655354) | 0x0062       |     19 |              5 |
| [65535.5](#event-655355) | 0x0075       |    113 |             12 |
| [65535.6](#event-655356) | 0x00E6       |     18 |              6 |
| [10137](#event-10137)    | 0x00F8       |      1 |              1 |
| [10161](#event-10161)    | 0x00F9       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0007      |           7 |
|       1 | 0x17A3      |        6051 |
|       2 | 0x1D7B6     |      120758 |
|       3 | 0x0998      |        2456 |
|       4 | 0x0000      |           0 |
|       5 | 0x215B      |        8539 |
|       6 | 0x00CE      |         206 |
|       7 | 0x001E      |          30 |
|       8 | 0x012C      |         300 |
|       9 | 0x000A      |          10 |
|      10 | 0x01FF      |         511 |
|      11 | 0x0096      |         150 |

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

### Event 10135

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

### Event 10136

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 29 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          33 01 32 00 80  22 01 37 01 80 02 80 03     3.2..".7.....
0010: 80 04 80 22 00 1F 00 05  80 02 80 03 80 1F 01 00  ..."............
```

#### Opcodes

```
  0: 0x0003 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0005 [0x32] ExtData[1]->MainSpeed = 7* * 0.1
  2: 0x0008 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x000A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=6.051*, z=120.758*, y=2.456*, direction=0.0°*
  4: 0x0013 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  5: 0x0015 [0x1F] MOVE_ENTITY: EventEntity moves to X=8.539*, Z=120.758*, Y=2.456*
  6: 0x001D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 46 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: AD 02 06 80 F8 FF FF 7F  F0 FF FF 7F 1C 07 80 AD  ................
0030: 02 06 80 F8 FF FF 7F F0  FF FF 7F 1C 07 80 AD 02  ................
0040: 06 80 F8 FF FF 7F F0 FF  FF 7F 1C 08 80 00        ..............  
```

#### Opcodes

```
  0: 0x0020 [0xAD] DUAL_ENTITY_SCHEDULER_HANDLER: Execute sub-case 2 with entities [EventEntity, LocalPlayer], work=206*
  1: 0x002C [0x1C] WAIT(30* ticks)
  2: 0x002F [0xAD] DUAL_ENTITY_SCHEDULER_HANDLER: Execute sub-case 2 with entities [EventEntity, LocalPlayer], work=206*
  3: 0x003B [0x1C] WAIT(30* ticks)
  4: 0x003E [0xAD] DUAL_ENTITY_SCHEDULER_HANDLER: Execute sub-case 2 with entities [EventEntity, LocalPlayer], work=206*
  5: 0x004A [0x1C] WAIT(300* ticks)
  6: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 20 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            33 01                3.
0050: 32 09 80 1F 00 01 80 02  80 03 80 1F 01 22 00 22  2............"."
0060: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x004E [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0050 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  2: 0x0053 [0x1F] MOVE_ENTITY: EventEntity moves to X=6.051*, Z=120.758*, Y=2.456*
  3: 0x005B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x005D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  5: 0x005F [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  6: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       32 00 80 1F 00 05  80 02 80 03 80 1F 01 1E    2.............
0070: 75 30 0F 01 00                                    u0...           
```

#### Opcodes

```
  0: 0x0062 [0x32] ExtData[1]->MainSpeed = 7* * 0.1
  1: 0x0065 [0x1F] MOVE_ENTITY: EventEntity moves to X=8.539*, Z=120.758*, Y=2.456*
  2: 0x006D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006F [0x1E] EventEntity looks at Nomad Moogle (ID: 17772661/0x010F3075) and starts talking
  4: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0075    |
| Data Size    | 113 bytes |
| Instructions | 12        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                52 0A 80  F0 FF FF 7F F0 FF FF 7F       R..........
0080: 30 32 30 6A 45 0A 80 F0  FF FF 7F F0 FF FF 7F 30  020jE..........0
0090: 32 30 6B 04 80 AD 02 06  80 F8 FF FF 7F F0 FF FF  20k.............
00A0: 7F 1C 07 80 AD 02 06 80  F8 FF FF 7F F0 FF FF 7F  ................
00B0: 1C 07 80 AD 02 06 80 F8  FF FF 7F F0 FF FF 7F 1C  ................
00C0: 0B 80 52 0A 80 F0 FF FF  7F F0 FF FF 7F 30 32 30  ..R..........020
00D0: 6B 45 0A 80 F0 FF FF 7F  F0 FF FF 7F 30 32 30 6C  kE..........020l
00E0: 04 80 1C 0B 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0075 [0x52] END_LOAD_SCHEDULER: End scheduler "020j" with entities [LocalPlayer, LocalPlayer], work=511*
  1: 0x0084 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "020k" with entities [LocalPlayer, LocalPlayer], work=[511*, 0*]
  2: 0x0095 [0xAD] DUAL_ENTITY_SCHEDULER_HANDLER: Execute sub-case 2 with entities [EventEntity, LocalPlayer], work=206*
  3: 0x00A1 [0x1C] WAIT(30* ticks)
  4: 0x00A4 [0xAD] DUAL_ENTITY_SCHEDULER_HANDLER: Execute sub-case 2 with entities [EventEntity, LocalPlayer], work=206*
  5: 0x00B0 [0x1C] WAIT(30* ticks)
  6: 0x00B3 [0xAD] DUAL_ENTITY_SCHEDULER_HANDLER: Execute sub-case 2 with entities [EventEntity, LocalPlayer], work=206*
  7: 0x00BF [0x1C] WAIT(150* ticks)
  8: 0x00C2 [0x52] END_LOAD_SCHEDULER: End scheduler "020k" with entities [LocalPlayer, LocalPlayer], work=511*
  9: 0x00D1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "020l" with entities [LocalPlayer, LocalPlayer], work=[511*, 0*]
 10: 0x00E2 [0x1C] WAIT(150* ticks)
 11: 0x00E5 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E6   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                   33 01  32 09 80 1F 00 04 80 02        3.2.......
00F0: 80 03 80 1F 01 22 01 00                           ....."..        
```

#### Opcodes

```
  0: 0x00E6 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x00E8 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  2: 0x00EB [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=120.758*, Y=2.456*
  3: 0x00F3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00F5 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  5: 0x00F7 [0x00] END_REQSTACK()
```

### Event 10137

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F8  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                          00                               .       
```

#### Opcodes

```
  0: 0x00F8 [0x00] END_REQSTACK()
```

### Event 10161

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F9  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                             00                             .      
```

#### Opcodes

```
  0: 0x00F9 [0x00] END_REQSTACK()
```
