# 17727590 - DoorRegines Magicmart

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 108 bytes                 |
| Total Events     | 2                         |
| References Count | 6                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     59 |             19 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D95      |        7573 |
|       1 | 0x001E      |          30 |
|       2 | 0x1D96      |        7574 |
|       3 | 0x1D97      |        7575 |
|       4 | 0x1D98      |        7576 |
|       5 | 0x1D99      |        7577 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 59 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 20 01 2B 14 80 0E  01 00 80 23 1C 01 80 2B   B .+......#...+
0010: 13 80 0E 01 02 80 23 1C  01 80 2B 14 80 0E 01 03  ......#...+.....
0020: 80 23 1C 01 80 2B 13 80  0E 01 04 80 23 1C 01 80  .#...+......#...
0030: 2B 14 80 0E 01 05 80 23  20 00 21 00              +......# .!.    
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0004 [0x2B] Rugiette (ID: 17727508/0x010E8014) [7573*]:
    → "Wait-- Did you hear that?"
  3: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000C [0x1C] WAIT(30* ticks)
  5: 0x000F [0x2B] Regine (ID: 17727507/0x010E8013) [7574*]:
    → "M-maybe it's a customer! At last!"
  6: 0x0016 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0017 [0x1C] WAIT(30* ticks)
  8: 0x001A [0x2B] Rugiette (ID: 17727508/0x010E8014) [7575*]:
    → "Another pauper, surely."
  9: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0022 [0x1C] WAIT(30* ticks)
 11: 0x0025 [0x2B] Regine (ID: 17727507/0x010E8013) [7576*]:
    → "Mind your manners, Rugiette! A customer is a customer, don't forget! And straighten up, please!!"
 12: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x002D [0x1C] WAIT(30* ticks)
 14: 0x0030 [0x2B] Rugiette (ID: 17727508/0x010E8014) [7577*]:
    → "Okay, okay! I'm standing, now, I'm standing."
 15: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0038 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 17: 0x003A [0x21] END_EVENT
 18: 0x003B [0x00] END_REQSTACK()
```
