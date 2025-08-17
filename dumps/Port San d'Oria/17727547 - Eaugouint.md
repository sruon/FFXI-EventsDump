# 17727547 - Eaugouint

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 132 bytes                 |
| Total Events     | 4                         |
| References Count | 7                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [4](#event-4)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     32 |              5 |
| [579](#event-579)        | 0x0022       |     36 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF5055  |  4294922325 |
|       1 | 0xFFFF6D7C  |  4294929788 |
|       2 | 0xFFFFF061  |  4294963297 |
|       3 | 0x0E5D      |        3677 |
|       4 | 0x0014      |          20 |
|       5 | 0x1DEE      |        7662 |
|       6 | 0x001E      |          30 |

## String References

- **7662**: Take a left to find the magic shop. Keep going straight for the residential area. Oh, and take care not to upset Regine; she's scary when she's mad!

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

### Event 4

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
| Data Size    | 32 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       92 01 F8 FF FF 7F  94 01 F8 FF FF 7F 79 00    ............y.
0010: F8 FF FF 7F 70 80 0E 01  37 00 80 01 80 02 80 03  ....p...7.......
0020: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0002 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0008 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000E [0x79] EventEntity looks at Ulmia (ID: 17727600/0x010E8070) (Basic look)
  3: 0x0018 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-44.971*, z=-37.508*, y=-3.999*, direction=323.2°*
  4: 0x0021 [0x00] END_REQSTACK()
```

### Event 579

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       1E F0 FF FF 7F 6F  70 66 04 80 F8 FF FF 7F    .....opf......
0030: F8 FF FF 7F 74 6C 6B 30  1D 05 80 23 5E 69 64 6C  ....tlk0...#^idl
0040: 30 1C 06 80 21 00                                 0...!.          
```

#### Opcodes

```
  0: 0x0022 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0027 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0028 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0029 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=7662*)
    → "Take a left to find the magic shop. Keep going straight for the residential area. Oh, and take care not to upset Regine; she's scary when she's mad!"
  5: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x003C [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0041 [0x1C] WAIT(30* ticks)
  8: 0x0044 [0x21] END_EVENT
  9: 0x0045 [0x00] END_REQSTACK()
```
