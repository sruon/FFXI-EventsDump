# 17744186 - Mog Dinghy

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Port Bastok (ID: 236) |
| Block Size       | 108 bytes             |
| Total Events     | 2                     |
| References Count | 4                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [440](#event-440)     | 0x0001       |     64 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x352F      |       13615 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x00C8      |         200 |

## String References

- **13615**: Move to a Mog Garden? [Most definitely!/Maybe not.]

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

### Event 440

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 64 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 24 00  80 01 80 01 80 25 02 00   .....$......%..
0010: 10 01 80 00 3A 00 03 01  10 02 80 02 00 00 01 80  ....:...........
0020: 01 37 00 45 03 80 F0 FF  FF 7F F0 FF FF 7F 66 64  .7.E..........fd
0030: 6F 31 01 80 01 37 00 01  3F 00 03 01 10 01 80 21  o1...7..?......!
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x24] CREATE_DIALOG(message_id=13615*, default_option=0*, option_flags=0*)
    → "Move to a Mog Garden? [Most definitely!/Maybe not.]"
  2: 0x000D [0x25] WAIT_DIALOG_SELECT()
  3: 0x000E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003A
  4: 0x0016 [0x03] Work_Zone[1] = 1*
  5: 0x001B [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0037
  6: 0x0023 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x0034 [0x01] GOTO 0x0037

SUBROUTINE_0037:
  8: 0x0037 [0x01] GOTO 0x003F
  9: 0x003A [0x03] Work_Zone[1] = 0*

SUBROUTINE_003F:
 10: 0x003F [0x21] END_EVENT
 11: 0x0040 [0x00] END_REQSTACK()
```
