# 17179463 - Kamlanaut

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 168 bytes                         |
| Total Events     | 11                                |
| References Count | 5                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [9](#event-9)            | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |      5 |              2 |
| [65535.2](#event-655352) | 0x000D       |      5 |              2 |
| [21](#event-21)          | 0x0012       |      4 |              2 |
| [22](#event-22)          | 0x0016       |      4 |              2 |
| [65535.3](#event-655353) | 0x001A       |      2 |              2 |
| [65535.4](#event-655354) | 0x001C       |     24 |              4 |
| [65535.5](#event-655355) | 0x0034       |     34 |              4 |
| [27](#event-27)          | 0x0056       |      1 |              1 |
| [28](#event-28)          | 0x0057       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0927      |        2343 |
|       1 | 0x058C      |        1420 |
|       2 | 0x0002      |           2 |
|       3 | 0x0069      |         105 |
|       4 | 0x0078      |         120 |

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
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          B6 00 00 80 00                   .....   
```

#### Opcodes

```
  0: 0x0008 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2343*)
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         B6 00 01               ...
0010: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x000D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1420*)
  1: 0x0011 [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       95 02 80 00                                   ....          
```

#### Opcodes

```
  0: 0x0012 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 2*)
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   95 02  80 00                          ....      
```

#### Opcodes

```
  0: 0x0016 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 2*)
  1: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                96 00                        ..    
```

#### Opcodes

```
  0: 0x001A [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      5B 03 80 F8              [...
0020: FF FF 7F F8 FF FF 7F 73  69 74 31 1C 04 80 5E 69  .......sit1...^i
0030: 64 6C 30 00                                       dl0.            
```

#### Opcodes

```
  0: 0x001C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sit1" with entities [EventEntity, EventEntity], work=105*
  1: 0x002B [0x1C] WAIT(120* ticks)
  2: 0x002E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  3: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             5B 03 80 F8  FF FF 7F F8 FF FF 7F 73      [..........s
0040: 69 74 30 53 F8 FF FF 7F  F8 FF FF 7F 73 69 74 30  it0S........sit0
0050: 5E 64 66 74 30 00                                 ^dft0.          
```

#### Opcodes

```
  0: 0x0034 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sit0" with entities [EventEntity, EventEntity], work=105*
  1: 0x0043 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sit0" with entities [EventEntity, EventEntity]
  2: 0x0050 [0x5E] EventEntity goes idle (kills current action) (animation: "dft0")
  3: 0x0055 [0x00] END_REQSTACK()
```

### Event 27

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0056  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   00                                    .         
```

#### Opcodes

```
  0: 0x0056 [0x00] END_REQSTACK()
```

### Event 28

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0057  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      00                                  .        
```

#### Opcodes

```
  0: 0x0057 [0x00] END_REQSTACK()
```
