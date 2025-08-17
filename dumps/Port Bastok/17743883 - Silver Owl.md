# 17743883 - Silver Owl

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Port Bastok (ID: 236) |
| Block Size       | 208 bytes             |
| Total Events     | 7                     |
| References Count | 6                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      6 |              2 |
| [150](#event-150)     | 0x0006       |     21 |              7 |
| [151](#event-151)     | 0x001B       |     31 |             11 |
| [152](#event-152)     | 0x003A       |     26 |              8 |
| [296](#event-296)     | 0x0054       |      1 |              1 |
| [459](#event-459)     | 0x0055       |     26 |              8 |
| [460](#event-460)     | 0x006F       |     27 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x1A56      |        6742 |
|       2 | 0x0079      |         121 |
|       3 | 0x1A57      |        6743 |
|       4 | 0x1A58      |        6744 |
|       5 | 0x1A59      |        6745 |

## String References

- **6742**: I have nothing to sell you.
- **6743**: Ah, you have come from headquarters. I will entrust you with $6. Take it back to headquarters.
- **6744**: You must leave your past behind--that is the way of the underworld.
- **6745**: Take $6 back to headquarters. You must leave your past behind--that is the way of the underworld.

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 03 00 00 00 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0000 [0x03] ExtData[1]->WorkLocal[0] = 1*
  1: 0x0005 [0x00] END_REQSTACK()
```

### Event 150

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0006   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   02 02  10 00 00 00 1A 00 20 01        ........ .
0010: 1E F0 FF FF 7F 1D 01 80  23 21 00                 ........#!.     
```

#### Opcodes

```
  0: 0x0006 [0x02] IF !(Work_Zone[2] == ExtData[1]->WorkLocal[0]) GOTO 0x001A
  1: 0x000E [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0010 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=6742*)
    → "I have nothing to sell you."
  4: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0019 [0x21] END_EVENT
  6: 0x001A [0x00] END_REQSTACK()
```

### Event 151

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 31 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   03 09 10 02 80             .....
0020: 02 02 10 00 00 00 39 00  20 01 42 1E F0 FF FF 7F  ......9. .B.....
0030: 1D 03 80 23 1D 04 80 23  21 00                    ...#...#!.      
```

#### Opcodes

```
  0: 0x001B [0x03] Work_Zone[9] = 121*
  1: 0x0020 [0x02] IF !(Work_Zone[2] == ExtData[1]->WorkLocal[0]) GOTO 0x0039
  2: 0x0028 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x002A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x002B [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0030 [0x1D] PRINT_EVENT_MESSAGE(message_id=6743*)
    → "Ah, you have come from headquarters. I will entrust you with $6. Take it back to headquarters."
  6: 0x0033 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0034 [0x1D] PRINT_EVENT_MESSAGE(message_id=6744*)
    → "You must leave your past behind--that is the way of the underworld."
  8: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0038 [0x21] END_EVENT
 10: 0x0039 [0x00] END_REQSTACK()
```

### Event 152

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                03 09 10 02 80 02            ......
0040: 02 10 00 00 00 53 00 20  01 1E F0 FF FF 7F 1D 05  .....S. ........
0050: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x003A [0x03] Work_Zone[9] = 121*
  1: 0x003F [0x02] IF !(Work_Zone[2] == ExtData[1]->WorkLocal[0]) GOTO 0x0053
  2: 0x0047 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x0049 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x004E [0x1D] PRINT_EVENT_MESSAGE(message_id=6745*)
    → "Take $6 back to headquarters. You must leave your past behind--that is the way of the underworld."
  5: 0x0051 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0052 [0x21] END_EVENT
  7: 0x0053 [0x00] END_REQSTACK()
```

### Event 296

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

### Event 459

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                4A F8 FF  FF 7F F0 FF FF 7F 4A F0       J........J.
0060: FF FF 7F F8 FF FF 7F 6F  70 1D 05 10 23 21 00     .......op...#!. 
```

#### Opcodes

```
  0: 0x0055 [0x4A] EventEntity looks at LocalPlayer
  1: 0x005E [0x4A] LocalPlayer looks at EventEntity
  2: 0x0067 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0068 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0069 [0x1D] PRINT_EVENT_MESSAGE(message_id=Work_Zone[5])
  5: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x006D [0x21] END_EVENT
  7: 0x006E [0x00] END_REQSTACK()
```

### Event 460

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               42                 B
0070: 4A F8 FF FF 7F F0 FF FF  7F 4A F0 FF FF 7F F8 FF  J........J......
0080: FF 7F 6F 70 1D 05 10 23  21 00                    ..op...#!.      
```

#### Opcodes

```
  0: 0x006F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0070 [0x4A] EventEntity looks at LocalPlayer
  2: 0x0079 [0x4A] LocalPlayer looks at EventEntity
  3: 0x0082 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0083 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=Work_Zone[5])
  6: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0088 [0x21] END_EVENT
  8: 0x0089 [0x00] END_REQSTACK()
```
