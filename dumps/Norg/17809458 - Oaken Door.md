# 17809458 - Oaken Door

## Common Data

| Field            | Value          |
|------------------|----------------|
| Zone             | Norg (ID: 252) |
| Block Size       | 168 bytes      |
| Total Events     | 20             |
| References Count | 2              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [175](#event-175)        | 0x0001       |      1 |              1 |
| [5](#event-5)            | 0x0002       |      1 |              1 |
| [2](#event-2)            | 0x0003       |      1 |              1 |
| [3](#event-3)            | 0x0004       |      1 |              1 |
| [65535.1](#event-655351) | 0x0005       |      2 |              2 |
| [65535.2](#event-655352) | 0x0007       |      2 |              2 |
| [146](#event-146)        | 0x0009       |      1 |              1 |
| [158](#event-158)        | 0x000A       |      1 |              1 |
| [164](#event-164)        | 0x000B       |      1 |              1 |
| [169](#event-169)        | 0x000C       |      1 |              1 |
| [172](#event-172)        | 0x000D       |      1 |              1 |
| [206](#event-206)        | 0x000E       |      1 |              1 |
| [65535.3](#event-655353) | 0x000F       |      2 |              2 |
| [65535.4](#event-655354) | 0x0011       |      2 |              2 |
| [235](#event-235)        | 0x0013       |     41 |              9 |
| [276](#event-276)        | 0x003C       |      1 |              1 |
| [278](#event-278)        | 0x003D       |      1 |              1 |
| [279](#event-279)        | 0x003E       |      1 |              1 |
| [290](#event-290)        | 0x003F       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x2C01      |       11265 |

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

### Event 175

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

### Event 5

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

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             00                                        .           
```

#### Opcodes

```
  0: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                4C 00                                   L.         
```

#### Opcodes

```
  0: 0x0005 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      4D  00                              M.       
```

#### Opcodes

```
  0: 0x0007 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0008 [0x00] END_REQSTACK()
```

### Event 146

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             00                             .      
```

#### Opcodes

```
  0: 0x0009 [0x00] END_REQSTACK()
```

### Event 158

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                00                           .     
```

#### Opcodes

```
  0: 0x000A [0x00] END_REQSTACK()
```

### Event 164

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   00                         .    
```

#### Opcodes

```
  0: 0x000B [0x00] END_REQSTACK()
```

### Event 169

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      00                       .   
```

#### Opcodes

```
  0: 0x000C [0x00] END_REQSTACK()
```

### Event 172

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         00                     .  
```

#### Opcodes

```
  0: 0x000D [0x00] END_REQSTACK()
```

### Event 206

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            00                   . 
```

#### Opcodes

```
  0: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               4C                 L
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x000F [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    4D 00                                           M.             
```

#### Opcodes

```
  0: 0x0011 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0012 [0x00] END_REQSTACK()
```

### Event 235

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 41 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          42 4A 11 C0 0F  01 F0 FF FF 7F 6F 76 11     BJ........ov.
0020: C0 0F 01 66 00 80 11 C0  0F 01 11 C0 0F 01 74 6C  ...f..........tl
0030: 6B 30 2B 11 C0 0F 01 01  80 23 21 00              k0+......#!.    
```

#### Opcodes

```
  0: 0x0013 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0014 [0x4A] Comitiolus (ID: 17809425/0x010FC011) looks at LocalPlayer
  2: 0x001D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x001E [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Comitiolus (ID: 17809425/0x010FC011) Render.Flags0 and Render.Flags3 conditions are met
  4: 0x0023 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Comitiolus (ID: 17809425/0x010FC011), Comitiolus (ID: 17809425/0x010FC011)], work=0*
  5: 0x0032 [0x2B] Comitiolus (ID: 17809425/0x010FC011) [11265*]:
    → "Sorry, <Player>, the boss is a little busy right now. Ye'll have to make yer meetin' fer another day."
  6: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x003A [0x21] END_EVENT
  8: 0x003B [0x00] END_REQSTACK()
```

### Event 276

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      00                       .   
```

#### Opcodes

```
  0: 0x003C [0x00] END_REQSTACK()
```

### Event 278

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         00                     .  
```

#### Opcodes

```
  0: 0x003D [0x00] END_REQSTACK()
```

### Event 279

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            00                   . 
```

#### Opcodes

```
  0: 0x003E [0x00] END_REQSTACK()
```

### Event 290

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
