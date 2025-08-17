# 17396171 - Torch Stand

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Castle Oztroja (ID: 151) |
| Block Size       | 104 bytes                |
| Total Events     | 2                        |
| References Count | 4                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [11](#event-11)       | 0x0001       |     61 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0002      |           2 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x0001      |           1 |

## String References

- **2**: Light the torch? [Yes./No.]

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

### Event 11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 61 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 01 80 00 31   $......%......1
0010: 00 42 43 00 43 01 27 00  D7 71 09 01 02 27 00 D8  .BC.C.'..q...'..
0020: 71 09 01 02 1C 02 80 29  00 F0 FF FF 7F 02 01 3C  q......).......<
0030: 00 02 00 10 03 80 00 3C  00 01 3C 00 21 00        .......<..<.!.  
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=2*, default_option=0*, option_flags=0*)
    → "Light the torch? [Yes./No.]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0031
  3: 0x0011 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x0012 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x0014 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x0016 [0x27] REQ_SET(priority=0x00, entity_id=Torch Stand (ID: 17396183/0x010971D7), tag_num=0x02)
  7: 0x001D [0x27] REQ_SET(priority=0x00, entity_id=Torch Stand (ID: 17396184/0x010971D8), tag_num=0x02)
  8: 0x0024 [0x1C] WAIT(60* ticks)
  9: 0x0027 [0x29] REQ_SET_WAIT(priority=0x00, entity_id=LocalPlayer, tag_num=0x02)
 10: 0x002E [0x01] GOTO 0x003C
 11: 0x0031 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x003C
 12: 0x0039 [0x01] GOTO 0x003C

SUBROUTINE_003C:
 13: 0x003C [0x21] END_EVENT
 14: 0x003D [0x00] END_REQSTACK()
```
