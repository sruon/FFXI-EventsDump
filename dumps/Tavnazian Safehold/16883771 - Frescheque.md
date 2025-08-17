# 16883771 - Frescheque

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 176 bytes                   |
| Total Events     | 11                          |
| References Count | 12                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [151](#event-151)        | 0x0001       |      1 |              1 |
| [154](#event-154)        | 0x0002       |      1 |              1 |
| [155](#event-155)        | 0x0003       |      1 |              1 |
| [65535.1](#event-655351) | 0x0004       |     32 |              7 |
| [171](#event-171)        | 0x0024       |      1 |              1 |
| [172](#event-172)        | 0x0025       |      1 |              1 |
| [174](#event-174)        | 0x0026       |      1 |              1 |
| [156](#event-156)        | 0x0027       |      6 |              4 |
| [157](#event-157)        | 0x002D       |     11 |              5 |
| [158](#event-158)        | 0x0038       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0078      |         120 |
|       1 | 0x6230      |       25136 |
|       2 | 0x2FCA      |       12234 |
|       3 | 0xFFFF72B7  |  4294931127 |
|       4 | 0x08F6      |        2294 |
|       5 | 0x000D      |          13 |
|       6 | 0x4D55      |       19797 |
|       7 | 0x3B2F      |       15151 |
|       8 | 0xFFFF7360  |  4294931296 |
|       9 | 0x290F      |       10511 |
|      10 | 0x296E      |       10606 |
|      11 | 0x296F      |       10607 |

## String References

- **10511**: <Sigh>
- **10606**: As long as we are bound by the past, we will never be able to step forward into the future. That is what I used to believe. However, now I realize that without the foundation the past has left us, our future will never stand.
- **10607**: The change the safehold has experienced recently... It has all been so sudden. However, we must learn to adapt and move on if we are to survive.

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

### Event 151

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

### Event 154

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

### Event 155

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 32 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             1C 00 80 4E  00 3B A0 01 01 37 01 80      ...N.;...7..
0010: 02 80 03 80 04 80 32 05  80 1F 00 06 80 07 80 08  ......2.........
0020: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0004 [0x1C] WAIT(120* ticks)
  1: 0x0007 [0x4E] SET_ENTITY_HIDE_FLAG: Show Frescheque (ID: 16883771/0x0101A03B)
  2: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=25.136*, z=12.234*, y=-36.169*, direction=201.6°*
  3: 0x0016 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  4: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=19.797*, Z=15.151*, Y=-36.000*
  5: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0023 [0x00] END_REQSTACK()
```

### Event 171

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             00                                        .           
```

#### Opcodes

```
  0: 0x0024 [0x00] END_REQSTACK()
```

### Event 172

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0025  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                00                                      .          
```

#### Opcodes

```
  0: 0x0025 [0x00] END_REQSTACK()
```

### Event 174

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0026  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   00                                    .         
```

#### Opcodes

```
  0: 0x0026 [0x00] END_REQSTACK()
```

### Event 156

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      1D  09 80 23 21 00                  ...#!.   
```

#### Opcodes

```
  0: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=10511*)
    → "<Sigh>"
  1: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x002B [0x21] END_EVENT
  3: 0x002C [0x00] END_REQSTACK()
```

### Event 157

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         1E F0 FF               ...
0030: FF 7F 1D 0A 80 23 21 00                           .....#!.        
```

#### Opcodes

```
  0: 0x002D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=10606*)
    → "As long as we are bound by the past, we will never be able to step forward into the future. That is what I used to believe. However, now I realize that without the foundation the past has left us, our future will never stand."
  2: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0036 [0x21] END_EVENT
  4: 0x0037 [0x00] END_REQSTACK()
```

### Event 158

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          1E F0 FF FF 7F 1D 0B 80          ........
0040: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0038 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=10607*)
    → "The change the safehold has experienced recently... It has all been so sudden. However, we must learn to adapt and move on if we are to survive."
  2: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0041 [0x21] END_EVENT
  4: 0x0042 [0x00] END_REQSTACK()
```
