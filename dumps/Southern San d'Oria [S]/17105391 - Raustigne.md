# 17105391 - Raustigne

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 212 bytes                        |
| Total Events     | 16                               |
| References Count | 9                                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [606](#event-606)        | 0x0001       |     41 |              7 |
| [55](#event-55)          | 0x002A       |      1 |              1 |
| [65535.1](#event-655351) | 0x002B       |     20 |              6 |
| [86](#event-86)          | 0x003F       |      1 |              1 |
| [87](#event-87)          | 0x0040       |      1 |              1 |
| [89](#event-89)          | 0x0041       |      1 |              1 |
| [147](#event-147)        | 0x0042       |      1 |              1 |
| [127](#event-127)        | 0x0043       |      1 |              1 |
| [169](#event-169)        | 0x0044       |      1 |              1 |
| [149](#event-149)        | 0x0045       |      1 |              1 |
| [65535.2](#event-655352) | 0x0046       |     21 |              5 |
| [148](#event-148)        | 0x005B       |      1 |              1 |
| [126](#event-126)        | 0x005C       |      1 |              1 |
| [186](#event-186)        | 0x005D       |      1 |              1 |
| [187](#event-187)        | 0x005E       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2F49      |       12105 |
|       2 | 0x000D      |          13 |
|       3 | 0x0B8B      |        2955 |
|       4 | 0xAA0A      |       43530 |
|       5 | 0xFFFFF831  |  4294965297 |
|       6 | 0x0036      |          54 |
|       7 | 0xB3D8      |       46040 |
|       8 | 0x0BB8      |        3000 |

## String References

- **12105**: Access beyond the Victory Gate is not permitted at this time.

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

### Event 606

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 41 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 66 00  80 F4 01 05 01 F4 01 05   .....f.........
0010: 01 74 6C 6B 30 1D 01 80  23 66 00 80 F4 01 05 01  .tlk0...#f......
0020: F4 01 05 01 74 6C 6B 31  21 00                    ....tlk1!.      
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Touttaures (ID: 17105396/0x010501F4), Touttaures (ID: 17105396/0x010501F4)], work=20*
  2: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=12105*)
    → "Access beyond the Victory Gate is not permitted at this time."
  3: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0019 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Touttaures (ID: 17105396/0x010501F4), Touttaures (ID: 17105396/0x010501F4)], work=20*
  5: 0x0028 [0x21] END_EVENT
  6: 0x0029 [0x00] END_REQSTACK()
```

### Event 55

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                00                           .     
```

#### Opcodes

```
  0: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   32 02 80 1F 00             2....
0030: 03 80 04 80 05 80 1F 01  6F 7B EF 01 05 01 00     ........o{..... 
```

#### Opcodes

```
  0: 0x002B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002E [0x1F] MOVE_ENTITY: EventEntity moves to X=2.955*, Z=43.530*, Y=-1.999*
  2: 0x0036 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0038 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0039 [0x7B] Raustigne (ID: 17105391/0x010501EF) stops talking
  5: 0x003E [0x00] END_REQSTACK()
```

### Event 86

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               00                 .
```

#### Opcodes

```
  0: 0x003F [0x00] END_REQSTACK()
```

### Event 87

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0040  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0040 [0x00] END_REQSTACK()
```

### Event 89

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0041  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    00                                              .              
```

#### Opcodes

```
  0: 0x0041 [0x00] END_REQSTACK()
```

### Event 147

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0042  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       00                                            .             
```

#### Opcodes

```
  0: 0x0042 [0x00] END_REQSTACK()
```

### Event 127

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0043  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          00                                          .            
```

#### Opcodes

```
  0: 0x0043 [0x00] END_REQSTACK()
```

### Event 169

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             00                                        .           
```

#### Opcodes

```
  0: 0x0044 [0x00] END_REQSTACK()
```

### Event 149

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                00                                      .          
```

#### Opcodes

```
  0: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   32 02  80 1F 00 06 80 07 80 05        2.........
0050: 80 1F 01 4B EF 01 05 01  08 80 00                 ...K.......     
```

#### Opcodes

```
  0: 0x0046 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.054*, Z=46.040*, Y=-1.999*
  2: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0053 [0x4B] UPDATE_ENTITY_YAW(entity=Raustigne (ID: 17105391/0x010501EF), yaw=16.5°*)
  4: 0x005A [0x00] END_REQSTACK()
```

### Event 148

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   00                         .    
```

#### Opcodes

```
  0: 0x005B [0x00] END_REQSTACK()
```

### Event 126

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      00                       .   
```

#### Opcodes

```
  0: 0x005C [0x00] END_REQSTACK()
```

### Event 186

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         00                     .  
```

#### Opcodes

```
  0: 0x005D [0x00] END_REQSTACK()
```

### Event 187

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            00                   . 
```

#### Opcodes

```
  0: 0x005E [0x00] END_REQSTACK()
```
