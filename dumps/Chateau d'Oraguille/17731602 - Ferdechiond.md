# 17731602 - Ferdechiond

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 420 bytes                     |
| Total Events     | 18                            |
| References Count | 17                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [9](#event-9)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [511](#event-511)        | 0x000C       |     36 |             10 |
| [89](#event-89)          | 0x0030       |     18 |              4 |
| [509](#event-509)        | 0x0042       |     10 |              2 |
| [563](#event-563)        | 0x004C       |      1 |              1 |
| [564](#event-564)        | 0x004D       |      1 |              1 |
| [578](#event-578)        | 0x004E       |      1 |              1 |
| [583](#event-583)        | 0x004F       |      1 |              1 |
| [586](#event-586)        | 0x0050       |      1 |              1 |
| [590](#event-590)        | 0x0051       |      1 |              1 |
| [591](#event-591)        | 0x0052       |      1 |              1 |
| [597](#event-597)        | 0x0053       |      1 |              1 |
| [604](#event-604)        | 0x0054       |      1 |              1 |
| [609](#event-609)        | 0x0055       |      1 |              1 |
| [65535.2](#event-655352) | 0x0056       |     90 |             17 |
| [65535.3](#event-655353) | 0x00B0       |     87 |             16 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0AD2      |        2770 |
|       1 | 0xFFFFE17A  |  4294959482 |
|       2 | 0x0000      |           0 |
|       3 | 0x0837      |        2103 |
|       4 | 0x0014      |          20 |
|       5 | 0x1C37      |        7223 |
|       6 | 0x001E      |          30 |
|       7 | 0xFFFF7190  |  4294930832 |
|       8 | 0x1383A     |       79930 |
|       9 | 0xFFFFF15B  |  4294963547 |
|      10 | 0x07C4      |        1988 |
|      11 | 0xFFFFF3FB  |  4294964219 |
|      12 | 0x246A      |        9322 |
|      13 | 0xFFFFFA25  |  4294965797 |
|      14 | 0x0200      |         512 |
|      15 | 0x000D      |          13 |
|      16 | 0x0001      |           1 |

## String References

- **7223**: The door beyond leads to the Temple Knights' quarters. The dungeons are down the corridor, to the left.

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

### Event 9

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
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=2.770*, z=-7.814*, y=0.000*, direction=184.8°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 511

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      1E F0 FF FF              ....
0010: 7F 6F 70 66 04 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .opf..........tl
0020: 6B 30 1D 05 80 23 5E 69  64 6C 30 1C 06 80 21 00  k0...#^idl0...!.
```

#### Opcodes

```
  0: 0x000C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0011 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0012 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0013 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=7223*)
    → "The door beyond leads to the Temple Knights' quarters. The dungeons are down the corridor, to the left."
  5: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0026 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x002B [0x1C] WAIT(30* ticks)
  8: 0x002E [0x21] END_EVENT
  9: 0x002F [0x00] END_REQSTACK()
```

### Event 89

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 22 01 92 01 F8 FF FF 7F  37 07 80 08 80 09 80 0A  ".......7.......
0040: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0030 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0032 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0038 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-36.464*, z=79.930*, y=-3.749*, direction=174.7°*
  3: 0x0041 [0x00] END_REQSTACK()
```

### Event 509

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       37 0B 80 0C 80 0D  80 0E 80 00                7.........    
```

#### Opcodes

```
  0: 0x0042 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-3.077*, z=9.322*, y=-1.499*, direction=45.0°*
  1: 0x004B [0x00] END_REQSTACK()
```

### Event 563

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      00                       .   
```

#### Opcodes

```
  0: 0x004C [0x00] END_REQSTACK()
```

### Event 564

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         00                     .  
```

#### Opcodes

```
  0: 0x004D [0x00] END_REQSTACK()
```

### Event 578

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            00                   . 
```

#### Opcodes

```
  0: 0x004E [0x00] END_REQSTACK()
```

### Event 583

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               00                 .
```

#### Opcodes

```
  0: 0x004F [0x00] END_REQSTACK()
```

### Event 586

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0050  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0050 [0x00] END_REQSTACK()
```

### Event 590

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0051  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    00                                              .              
```

#### Opcodes

```
  0: 0x0051 [0x00] END_REQSTACK()
```

### Event 591

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0052  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       00                                            .             
```

#### Opcodes

```
  0: 0x0052 [0x00] END_REQSTACK()
```

### Event 597

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0053  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          00                                          .            
```

#### Opcodes

```
  0: 0x0053 [0x00] END_REQSTACK()
```

### Event 604

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0054  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             00                                        .           
```

#### Opcodes

```
  0: 0x0054 [0x00] END_REQSTACK()
```

### Event 609

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0055  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                00                                      .          
```

#### Opcodes

```
  0: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 90 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   6E F8  FF FF 7F 0F 80 99 F8 FF        n.........
0060: FF 7F 06 04 00 3B F8 FF  FF 7F 00 00 02 00 03 00  .....;..........
0070: 3B 34 90 0E 01 00 00 01  00 03 00 02 01 00 02 00  ;4..............
0080: 03 94 00 3B 34 90 0E 01  00 00 01 00 03 00 1C 10  ...;4...........
0090: 80 01 7B 00 5E 69 64 6C  30 1C 06 80 1E 34 90 0E  ..{.^idl0....4..
00A0: 01 6F 70 6E F8 FF FF 7F  0F 80 99 F8 FF FF 7F 00  .opn............
```

#### Opcodes

```
  0: 0x0056 [0x6E] EventEntity uses emote 13*
  1: 0x005D [0x99] Wait for EventEntity animation to complete
  2: 0x0062 [0x06] ExtData[1]->WorkLocal[4] = 0
  3: 0x0065 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  4: 0x0070 [0x3B] GET_ENTITY_POSITION(entity=Exoroche (ID: 17731636/0x010E9034), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[3])
  5: 0x007B [0x02] IF !(ExtData[1]->WorkLocal[1] >= ExtData[1]->WorkLocal[2]) GOTO 0x0094
  6: 0x0083 [0x3B] GET_ENTITY_POSITION(entity=Exoroche (ID: 17731636/0x010E9034), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[3])
  7: 0x008E [0x1C] WAIT(1* ticks)
  8: 0x0091 [0x01] GOTO 0x007B
  9: 0x0094 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 10: 0x0099 [0x1C] WAIT(30* ticks)
 11: 0x009C [0x1E] EventEntity looks at Exoroche (ID: 17731636/0x010E9034) and starts talking
 12: 0x00A1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 13: 0x00A2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 14: 0x00A3 [0x6E] EventEntity uses emote 13*
 15: 0x00AA [0x99] Wait for EventEntity animation to complete
 16: 0x00AF [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 87 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 6E F8 FF FF 7F 0F 80 99  F8 FF FF 7F 3B F8 FF FF  n...........;...
00C0: 7F 00 00 02 00 03 00 3B  34 90 0E 01 00 00 01 00  .......;4.......
00D0: 03 00 02 01 00 02 00 02  EB 00 3B 34 90 0E 01 00  ..........;4....
00E0: 00 01 00 03 00 1C 10 80  01 D2 00 5E 69 64 6C 30  ...........^idl0
00F0: 1C 06 80 1E 34 90 0E 01  6F 70 6E F8 FF FF 7F 0F  ....4...opn.....
0100: 80 99 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x00B0 [0x6E] EventEntity uses emote 13*
  1: 0x00B7 [0x99] Wait for EventEntity animation to complete
  2: 0x00BC [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  3: 0x00C7 [0x3B] GET_ENTITY_POSITION(entity=Exoroche (ID: 17731636/0x010E9034), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[3])
  4: 0x00D2 [0x02] IF !(ExtData[1]->WorkLocal[1] <= ExtData[1]->WorkLocal[2]) GOTO 0x00EB
  5: 0x00DA [0x3B] GET_ENTITY_POSITION(entity=Exoroche (ID: 17731636/0x010E9034), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[3])
  6: 0x00E5 [0x1C] WAIT(1* ticks)
  7: 0x00E8 [0x01] GOTO 0x00D2
  8: 0x00EB [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  9: 0x00F0 [0x1C] WAIT(30* ticks)
 10: 0x00F3 [0x1E] EventEntity looks at Exoroche (ID: 17731636/0x010E9034) and starts talking
 11: 0x00F8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 12: 0x00F9 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 13: 0x00FA [0x6E] EventEntity uses emote 13*
 14: 0x0101 [0x99] Wait for EventEntity animation to complete
 15: 0x0106 [0x00] END_REQSTACK()
```
